# os
import os

# log
import logging

# django
import django
from django.conf import settings

# discord
import discord
from discord.ext import commands
from pretty_help import PrettyHelp

# from discord_slash import SlashCommand
# import discord_slash

REACTION_SUCCESS = 'OUO'
REACTION_FAILURE = ';('
HOLDER_ID = 995205064954236959

TOKEN = os.getenv('SAC_2045_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
# 紀錄log
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teabeBot.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
# logger = logging.getLogger('bot')
django.setup()

# logger.info('Starting up bot')
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='/', intents=intents)
# slash = SlashCommand(bot, sync_commands=True, sync_on_cog_reload=True)
# slash = SlashCommand(bot, sync_commands=True, sync_on_cog_reload=True, override_type=True, delete_from_unused_guilds=True)# 強制更新

# menu = DefaultMenu(active_time=60)
# ending_note = "{ctx.bot.user.name}的使用說明"
# bot.help_command = PrettyHelp(menu=menu, ending_note=ending_note)

def checkPath(extension):
    if os.path.isdir(extension) == False:
        return None
    mypath = '{}/bot_commands'.format(extension)
    reload_path = '{}.bot_commands'.format(extension)
    if os.path.isdir(mypath) == False:
        return None
    return mypath, reload_path

@bot.command(name='load', hidden=True)
async def load(ctx, app, extension=None):
    "開發 新增使用"
    await load_handle(ctx=ctx, botAction=bot.load_extension, app=app, extension=extension)

@bot.command(name='unload', hidden=True)
async def unload(ctx, app, extension=None):
    "開發 移除使用"
    await load_handle(ctx=ctx, botAction=bot.unload_extension, app=app, extension=extension)

@bot.command(name='reload', hidden=True)
async def reload(ctx, app, extension=None):
    "開發 重新讀取使用"
    await load_handle(ctx=ctx, botAction=bot.reload_extension, app=app, extension=extension)

async def load_handle(ctx, botAction, app, extension=None):
    if ctx.author.id == HOLDER_ID:
        mypath, reload_path = checkPath(app)
        if not mypath:
            await ctx.message.add_reaction(REACTION_FAILURE)
            return
        if extension:
            try:
                botAction('{}.{}'.format(reload_path, extension))
            except Exception as e:
                await ctx.message.add_reaction(REACTION_FAILURE)
            await ctx.message.add_reaction(REACTION_SUCCESS)
            return
        for filename in os.listdir(mypath):
            if filename.endswith('.py') == False:
                continue
            try:
                # eat bot_commands/XXXX.py
                botAction('{}.{}'.format(reload_path, filename[:-3]))
            except Exception as e:
                pass
                # logger.error('import commit error: {}'.format(e))
        await ctx.message.add_reaction(REACTION_SUCCESS)

for installed_app in settings.INSTALLED_APPS:
    app = installed_app.split('.')[0]
    if os.path.isdir(app) == False:
        continue
    mypath = '{}/bot_commands'.format(app)
    if os.path.isdir(mypath) == False:
        continue
    for filename in os.listdir(mypath):
        if filename.endswith('.py') == False:
            continue
        # eat bot_commands/XXXX.py
        try:
            print('{}.bot_commands.{}'.format(app, filename[:-3]))
            bot.load_extension('{}.bot_commands.{}'.format(app, filename[:-3]))
        except Exception as e:
            pass
            # logger.error('import commit error: {}'.format(e))

bot.run(TOKEN)

