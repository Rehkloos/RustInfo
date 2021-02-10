import iso8601
import discord
import requests
import os
from datetime import datetime
from urllib.parse import unquote
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from dotenv import load_dotenv

load_dotenv()
BMSID = os.getenv('battleMetricsServerID')


def BattleMetricsAPI():
    URL = "https://api.battlemetrics.com/servers/9908382"
    response = requests.get(URL)
    return response.json()


class ServerInfo(commands.Cog, name='Rust'):
    def __init__(self, bot):
        self.bot = bot

    #  RustyCorns server info
    @commands.command(name='!rustycorns - RustyCorns Server info',
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
        embed.set_footer(icon_url=self.context.bot.user.avatar_url, text=f'Called by: {self.context.author}')

        await ctx.send(file=file, embed=embed)

    #  RustyCorns server info
    @commands.command(name='!rcstatus - RustyCorns Status',
                      aliases=['rcstatus'],
                      help='RustyCorns server status')
    @commands.cooldown(2, 60, BucketType.user)
    async def server_status(self, ctx):

        header = ""
        title = ""
        url = ""
        responseJSON = BattleMetricsAPI()

        # JSON Results Mapping
        header = responseJSON['data']['attributes']['details']['rust_maps']['url']
        embed_image = responseJSON['data']['attributes']['details']['rust_maps']['thumbnailUrl']
        maps = responseJSON['data']['attributes']['details']['map']

        title = responseJSON['data']['attributes']['name']
        desc = responseJSON['data']['attributes']['details']['rust_description']
        url = responseJSON['data']['attributes']['details']['rust_url']
        fps = responseJSON['data']['attributes']['details']['rust_fps']
        fpsavg = responseJSON['data']['attributes']['details']['rust_fps_avg']
        rust_type = responseJSON['data']['attributes']['details']['rust_type']
        rust_uptime = responseJSON['data']['attributes']['details']['rust_uptime']
        rust_status = responseJSON['data']['attributes']['status']
        rust_world_size = responseJSON['data']['attributes']['details']['rust_world_size']
        rust_world_seed = responseJSON['data']['attributes']['details']['rust_world_seed']
        # players = responseJSON['data']['attributes']['details']['players']
        last_wipe = responseJSON['data']['attributes']['details']['rust_last_wipe']

        #convert iso8601 format
        is8061 = ""
        is8061 = iso8601.parse_date(last_wipe)

        # get country flag iso code
        country = responseJSON['data']['attributes']['country']
        if country == 'US':
            flag = (u"\U0001F1FA\U0001F1F8" + " " + country)

        embed = discord.Embed(
            title=title,
            description='\n\n' + header + '\n\n',
            # crimson color code
            colour=(0xDC143C)
        )
        embed.set_image(url=embed_image)
        file = discord.File("./assets/images/rust_honeycomb.png", filename="rust_honeycomb.png")
        embed.set_thumbnail(url="attachment://rust_honeycomb.png")
        embed.add_field(name="Status", value=(rust_status), inline=True)
        embed.add_field(name=("Type"), value=(rust_type), inline=True)
        embed.add_field(name=('FPS'), value=(fpsavg), inline=True)
        embed.add_field(name=('Rust World Size'), value=(rust_world_size), inline=True)
        embed.add_field(name=('Rust World Seed'), value=(rust_world_seed), inline=True)
        embed.add_field(name=('Last Wipe'), value=(is8061), inline=True)
        embed.add_field(name=('Country'), value=(flag), inline=True)
        embed.set_footer(icon_url=self.context.bot.user.avatar_url, text=f'Called by: {self.context.author}')

        await ctx.send(file=file, embed=embed)


def setup(bot):
    bot.add_cog(ServerInfo(bot))
