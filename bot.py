import discord
import requests
import aiohttp
from discord.ext import commands
from discord.ext import tasks
import os

import sys
import traceback
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD')
BMSID = os.getenv('battleMetricsServerID')

#rustycorns
# battleMetricsServerID = 9908382


def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefixes = ['!']

    # Check to see if we are outside of a guild. e.g DM's etc.
    if not message.guild:
        # Only allow ? to be used in DMs
        return '?'

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)


bot = commands.Bot(command_prefix=get_prefix,
                   description='A Rewrite Cog Example')
bot.remove_command('help')


# This is what we're going to use to load the cogs on startup
if __name__ == '__main__':
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):  # We only want to check through the python files
         try:  # I'd rather have this try/except block as I'd like it to load even if there is an issue with the cogs
            # This will load it
            bot.load_extension("cogs.{0}".format(filename[:-3]))
            # this is to let us know which cogs got loaded
            print("{0} is online".format(filename[:-3]))
         except:
            print("{0} was not loaded".format(filename))
            continue

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        pass


@bot.event
async def on_ready():
    print(f"Bot successfully started\n")
    change_status.start()

@tasks.loop(seconds=60)
async def change_status():
    serverData = await makeWebRequest(f"https://api.battlemetrics.com/servers/" + BMSID)
    if serverData == None:
        return

    serverPlayers = serverData['data']['attributes']['players']
    serverMaxPlayers = serverData['data']['attributes']['maxPlayers']
    serverQueue = serverData['data']['attributes']['details']['rust_queued_players']

    if serverQueue > 0:
        await bot.change_presence(activity=discord.Game(f"{serverPlayers}/{serverMaxPlayers} Queue {serverQueue}"))
    else:
        await bot.change_presence(activity=discord.Game(f"{serverPlayers}/{serverMaxPlayers}"))

async def makeWebRequest(URL):
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as preJSData:
            if preJSData.status == 200:
                return await preJSData.json()
            else:
                print(f"BattleMetrics Error [Code {preJSData.status}]")


bot.run(TOKEN, bot=True, reconnect=True)
