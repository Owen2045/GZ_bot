import logging
import os
import random
import asyncio
import discord
import django
import interactions
from discord.ext import commands
from django.conf import settings
from dotenv import load_dotenv
from pretty_help import EmojiMenu, PrettyHelp

load_dotenv()
# 環境變數
TOKEN = os.getenv('The_Crane_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
os.environ.setdefault('DJANGO_SETTINGS_MODULE',  'GZ_bot.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
logger = logging.getLogger('bot')
django.setup()

# client 是我們與 Discord 連結的橋樑
intents = discord.Intents.default()
# intents = 權限
intents.members = True
intents.message_content = True
intents.messages = True
# client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="!", intents=intents)

menu = EmojiMenu(active_time=60)
ending_note = "{ctx.bot.user.name}的使用說明"
bot.help_command = PrettyHelp(menu=menu, ending_note=ending_note)


@bot.event
async def on_ready():
    print('目前登入身份：', bot.user)
    game = discord.Game('與你媽在SWAG上見面')
    await bot.change_presence(status=discord.Status.online, activity=game)
    for guild in bot.guilds:
        if guild.name == GUILD:
            print(f'guild_name: {guild.name}  guild_id: {guild.id}')
            break


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f' {member.name}, 玩砸了'
    )


@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f"cmds.{extension}")

@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f"cmds.{extension}")




# async def load_handle(ctx, botAction, app, extension=None):
#     if ctx.author.id == HOLDER_ID:
#         mypath, reload_path = checkPath(app)
#         if not mypath:
#             await ctx.message.add_reaction(REACTION_FAILURE)
#             return
#         if extension:
#             try:
#                 botAction('{}.{}'.format(reload_path, extension))
#             except Exception as e:
#                 await ctx.message.add_reaction(REACTION_FAILURE)
#             await ctx.message.add_reaction(REACTION_SUCCESS)
#             return
#         for filename in os.listdir(mypath):
#             if filename.endswith('.py') == False:
#                 continue
#             try:
#                 # eat bot_commands/XXXX.py
#                 botAction('{}.{}'.format(reload_path, filename[:-3]))
#             except Exception as e:
#                 logger.error('import commit error: {}'.format(e))
#         await ctx.message.add_reaction(REACTION_SUCCESS)



# 讀取指令
async def load_extensions():
    for installed_app in settings.INSTALLED_APPS:
        app = installed_app.split('.')[0]
        if os.path.isdir(app) == False:
            continue
        mypath = f'{app}/bot_commands'
        if os.path.isdir(mypath) == False:
            continue
        for filename in os.listdir(mypath):
            if filename.endswith('.py') == False:
                continue
            # EX: bot_commands/XXXX.py
            fn = f'{app}.bot_commands.{filename[:-3]}'
            print(fn)
            await bot.load_extension(fn)
    await bot.start(TOKEN)

# async def main():
#     async with bot:
#         await bot.load_extension()
#         await bot.start(TOKEN)

asyncio.run(load_extensions())


# bot.run(TOKEN)