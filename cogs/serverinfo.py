import discord
import requests
from datetime import datetime
from urllib.parse import unquote
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType


def BattleMetricsAPI():
    URL = "https://api.battlemetrics.com/servers/9908382"
    response = requests.get(URL)
    return response.json()


class ServerInfo(commands.Cog, name='Rust'):
    def __init__(self, bot):
        self.bot = bot

    #  RustyCorns server info
    @commands.command(name='RustyCorns Server info',
                      aliases=['rustycorns'],
                      help='RustyCorns server info')
    @commands.cooldown(2, 60, BucketType.user)
    async def rustinfo(self, ctx):

        header = ""
        title = ""
        url = ""
        responseJSON = BattleMetricsAPI()

        # JSON Results Mapping
        header = responseJSON['data']['attributes']['details']['rust_headerimage']
        title = responseJSON['data']['attributes']['name']
        desc = responseJSON['data']['attributes']['details']['rust_description']
        url = responseJSON['data']['attributes']['details']['rust_url']

        embed = discord.Embed(
            title=title,
            description='***' + desc + '***' + '\n\n' + url,
            # crimson color code
            colour=(0xDC143C)
        )
        embed.set_image(url=header)
        file = discord.File("./assets/images/rust_honeycomb.png", filename="rust_honeycomb.png")
        embed.set_thumbnail(url="attachment://rust_honeycomb.png")

        await ctx.send(file=file, embed=embed)

    # #  RustyCorns server info
    # @commands.command(name='RustyCorns Server info',
    #                   aliases=['rcstatus'],
    #                   help='RustyCorns server status')
    # @commands.cooldown(2, 60, BucketType.user)
    # async def server_status(self, ctx):

    #     header = ""
    #     title = ""
    #     url = ""
    #     responseJSON = BattleMetricsAPI()

    #     # JSON Results Mapping
    #     header = responseJSON['data']['attributes']['details']['rust_headerimage']
    #     title = responseJSON['data']['attributes']['name']
    #     desc = responseJSON['data']['attributes']['details']['rust_description']
    #     url = responseJSON['data']['attributes']['details']['rust_url']
    #     fps = responseJSON['data']['attributes']['details']['rust_fps']
    #     fpsavg = responseJSON['data']['attributes']['details']['rust_fps_avg']
    #     rust_type = responseJSON['data']['attributes']['details']['rust_type']
    #     rust_uptime = responseJSON['data']['attributes']['details']['rust_uptime']

    #     embed = discord.Embed(
    #         title=title,
    #         description='***' + desc + '***' + '\n\n' + url,
    #         # crimson color code
    #         colour=(0xDC143C)
    #     )
    #     embed.set_image(url=header)
    #     file = discord.File("./assets/images/rust_honeycomb.png", filename="rust_honeycomb.png")
    #     embed.set_thumbnail(url="attachment://rust_honeycomb.png")
    #     # embed.add_field(name="Total Time Played", value=(TTP), inline=True)
    #     # embed.add_field(name=('Kills'), value=(kills), inline=True)
    #     # embed.add_field(name=("Deaths"), value=(deaths), inline=True)
    #     # embed.add_field(name="Wins", value=(wins), inline=True)
    #     # embed.add_field(name="Win %", value=(winr), inline=True)
    #     # embed.add_field(name="KDR", value=(kdr), inline=True)
    #     # embed.add_field(name="Assists", value=(asst), inline=True)
    #     # embed.add_field(name="Matches", value=(matches), inline=True)
    #     # embed.add_field(name="Headshots", value=(headshots), inline=True)
    #     # embed.add_field(name="Headshots %", value=(headshotpercentage), inline=True)
    #     # embed.add_field(name="First Bloods", value=(firstbloods), inline=True)
    #     # embed.add_field(name="Aces", value=(aces), inline=True)
    #     # embed.add_field(name="Clutches", value=(clutches), inline=True)
    #     # embed.add_field(name="Flawless", value=(flawless), inline=True)
    #     # embed.add_field(name=" .", value=(". "), inline=True)

    #     await ctx.send(file=file, embed=embed)


def setup(bot):
    bot.add_cog(ServerInfo(bot))
