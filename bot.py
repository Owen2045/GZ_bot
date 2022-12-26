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
import lightbulb
import hikari

load_dotenv()
# 環境變數
TOKEN = os.getenv('The_Crane_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
os.environ.setdefault('DJANGO_SETTINGS_MODULE',  'GZ_bot.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
logger = logging.getLogger('bot')
django.setup()

# intents = discord.Intents.default()
# intents = 權限
# intents.members = True
# intents.message_content = True
# intents.messages = True
# client = discord.Client(intents=intents)
# bot = commands.Bot(command_prefix="!", intents=intents)

# menu = EmojiMenu(active_time=60)
# ending_note = "{ctx.bot.user.name}的使用說明"
# bot.help_command = PrettyHelp(menu=menu, ending_note=ending_note)


bot = lightbulb.BotApp(token=TOKEN, default_enabled_guilds=(995205064954236959))

# 啟動訊息
@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('bot has started')


# 指令
@bot.command
@lightbulb.command(name='ping', description='Say Bonk!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('bonk!')


# sub 指令
@bot.command
@lightbulb.command(name='fuck', description='#fuck 2022')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def fuck_2022(ctx):
    pass

@fuck_2022.child
@lightbulb.command(name='job', description='fuck your job')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def job(ctx):
    await ctx.respond('fuck yeshome')


# 傳參數
@bot.command
@lightbulb.option(name='num1', description='輸入第一個數字', type=int)
@lightbulb.option(name='num2', description='輸入第二個數字', type=int)
@lightbulb.command(name='add', description='相加人')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)


bot.load_extensions_from('./GZ_info/bot_commands')





# 啟動
bot.run()

