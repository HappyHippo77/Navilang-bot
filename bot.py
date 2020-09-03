import discord
from discord.ext import commands
import config

client = discord.Client()

bot = commands.Bot(command_prefix=config.prefix, description=config.description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-------------------')
    await bot.change_presence(activity=discord.Game(name=config.status + " V" + config.version))
    print('status set.')
    print('-------------------')


@bot.event
async def on_message(message):
    if message.content.startswith(config.prefix + 'help'):
        await message.author.send(embed=discord.Embed(description=config.help, colour=0x5b2076))
    if "’" in message.content:
        message.content = message.content.replace("’", "\'")
    await bot.process_commands(message)


@bot.command()
async def horen(ctx):
    if ctx.message.author.id in config.operators:
        await ctx.send(embed=discord.Embed(description="Nothing here yet...", colour=0xff0000))

client.run(config.token)