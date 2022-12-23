import discord
import os
import random
import interactions
from dotenv import load_dotenv
from discord.ext import commands
from pretty_help import PrettyHelp, EmojiMenu

load_dotenv()
# 環境變數
TOKEN = os.getenv('The_Crane_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# client 是我們與 Discord 連結的橋樑
intents = discord.Intents.default()
# intents = 權限
intents.members = True
intents.message_content = True
intents.messages = True
# client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="!", intents=intents)
# bot = interactions.Client(command_prefix='!', token=TOKEN, intents=intents)

# @client.event
# # bot 啟動設定訊息
# async def on_ready():
#     print('目前登入身份：', client.user)
#     print(TOKEN)
#     game = discord.Game('與你媽在SWAG上見面')
#     await client.change_presence(status=discord.Status.online, activity=game)
#     for guild in client.guilds:
#         if guild.name == GUILD:
#             break
#     print(f'{guild.name}(id: {guild.id})')

@bot.event
async def on_ready():
    print("Bot in ready")



# # 加入伺服器通知
# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f' {member.name}, welcome to hell'
#     )


@bot.command()
async def hello(ctx):
    await ctx.send(f"!Hi <@{ctx.author.id}>")

# @client.event
# # 訊息事件
# async def on_message(message):
#     # 排除自己的訊息，避免陷入無限循環
#     if message.author == client.user:
#         return
#     #如果包含 ping，機器人回傳 pong
#     if message.content == 'ping':
#         await message.channel.send('pog')

#     if message.content.startswith('史粉'):
#         channel = message.channel
#         #機器人叫你先跟他說你好
#         await channel.send('逼逼逼...績優蒿難喝...')
#         #檢查函式，確認使用者是否在相同頻道打上「你好」
#         def checkmessage(m):
#             return m.content == '你好' and m.channel == channel
#         #獲取傳訊息的資訊(message是類型，也可以用reaction_add等等動作)
#         msg = await client.wait_for('message', check=checkmessage)
#         await channel.send('嗨, {.author}!'.format(msg))


# client.run(TOKEN)
bot.run(TOKEN)