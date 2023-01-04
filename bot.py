import logging
import os
import random
import asyncio
import discord
import django
import interactions
from discord.ext import commands
from django.conf import settings
from GZ_info.bot_settings import choose_colour
from dotenv import load_dotenv
from pretty_help import EmojiMenu, PrettyHelp
import lightbulb
import hikari

load_dotenv()
# 環境變數
TOKEN = os.getenv('The_Crane_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
HOLDER_ID = os.getenv('HOLDER_ID')
DF_GUILDS = os.getenv('DF_GUILDS')

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


bot = lightbulb.BotApp(token=TOKEN, default_enabled_guilds=(DF_GUILDS,)) # , help_slash_command=True, intents=hikari.Intents.ALL

# 啟動訊息
@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('bot has started')
    # logger.info(f'bot is start, HOLDER_ID: {HOLDER_ID} DF_GUILDS: {DF_GUILDS}')




# **==========example commands==========**
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
# **=====================**


# reload
@bot.command
# @lightbulb.option(name='extension', description='重載指定指令')
@lightbulb.option(name='app', description='重載指定指令')
@lightbulb.command(name='reload', description='重載指令')
@lightbulb.implements(lightbulb.SlashCommand)
async def reload(ctx):
    app = ctx.options.app.replace(" ", "_")
    succ = []
    nload = []
    exc = []
    mypath = f'{app}/bot_commands'
    if os.path.isdir(mypath):
        for filename in os.listdir(mypath):
            if filename.endswith('.py'):
                filename = filename.replace('.py', '')
                reload_file = f'{app}.bot_commands.{filename}'
                try:
                    # ctx.bot.reload_extensions("GZ_info.bot_commands.example_commans")
                    ctx.bot.reload_extensions(reload_file)
                    succ_msg = f'{app}.{filename}'
                    succ.append(succ_msg)

                except lightbulb.ExtensionNotLoaded:
                    nload_msg = f'{app}.{filename}'
                    nload.append(nload_msg)

                except Exception as exc:
                    exc_msg = f'{app}.{filename}'
                    exc.append(exc_msg)

    await ctx.respond(hikari.Embed(
                        title="reload", 
                        description='\n'.join(succ), 
                        color=choose_colour())
                    )


# 讀app所有指令
for installed_app in settings.INSTALLED_APPS:
    app = installed_app.split('.')[0]
    if os.path.isdir(app) == False:
        continue
    mypath = f'{app}/bot_commands'
    if os.path.isdir(mypath) == False:
        continue
    extensions_file = f'./{app}/bot_commands'
    try:
        bot.load_extensions_from(extensions_file)
        # logger.info(f'command load: {extensions_file}')
    except Exception as e:
        print(e)
        # logger.warning(f'load command warning: {extensions_file}')

# bot.load_extensions_from('./GZ_info/bot_commands')


# 啟動
bot.run(
    activity=hikari.Activity(
        name='正與你媽在SWAG上見面',
        type=hikari.ActivityType.COMPETING,
    )
)

