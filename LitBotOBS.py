import discord
from discord.ext import commands
import aysncio

@commands.command()
async def join(self, ctx, *, channel: discord.VoiceChannel):
    if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

    await channel.connect()

@commands.command()
async def stop(self, ctx):

    await ctx.voice_client.disconnect()

@commands.command()
async def members(ctx):

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!")

@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))
    print('------')

bot.run('my token')
