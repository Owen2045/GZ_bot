import asyncio
import time
import miru
import hikari
import lightbulb
import pandas as pd
from psutil import Process, virtual_memory

from googletrans import Translator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from GZ_info.models import UpdateInfo
from GZ_info.bot_settings import YesButton, SelectMenu, ExitButton

plugin = lightbulb.Plugin('Info')

@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_messages(event):
    pass




# 爬週末活動
def get_WE_info():
    res = ''
    try:
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--headless")
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        browser.get('https://gamezbd-info.pages.dev/timer')
        div3 = browser.find_element(By.XPATH, '//*[@id="q-app"]/div/div[2]/div[1]/main/div/div[2]/div')
        res = div3.text
    except Exception as e:
        pass
    return res

# 翻譯
def do_trans(data_str):
    ev_info = 'get data fail ;('
    if isinstance(data_str, str):
        str_list = data_str.split('\n')
        translator = Translator()
        zh_obj_list = translator.translate(str_list, dest='zh-tw')
        zh_list = [x.text for x in zh_obj_list if x]
        ev_info = '\n'.join(zh_list[:-1])
    return ev_info

# 取更新資訊
def get_update_info():
    qs = UpdateInfo.objects.all().order_by('-id').values('info_time', 'info_time_str', 'update_info_en', 'update_info_zh', 'url')
    df = pd.DataFrame(qs, dtype=object)
    date_list = df['info_time_str'].tolist()
    return date_list, df


@plugin.command
@lightbulb.command(name='info', description='週末加倍資訊', auto_defer=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def info(ctx):
    result_en = get_WE_info()
    result_zh = do_trans(result_en)
    await ctx.respond(result_zh) # , hikari.ResponseType.DEFERRED_MESSAGE_CREATE 


@plugin.command
@lightbulb.command(name='patch', description='更新資訊') # , auto_defer=True
@lightbulb.implements(lightbulb.SlashCommand)
async def patch(ctx):
    date_list, df = get_update_info()
    # view = BasicView(timeout=100) # 使用自定義view
    view = miru.View(timeout=100)
    view.add_item(SelectMenu(df=df, options=[miru.SelectOption(label=x) for x in date_list]))
    view.add_item(ExitButton(style=hikari.ButtonStyle.DANGER, label="結束查詢"))  
    message = await ctx.respond("選擇你的書記", components=view)
    await view.start(message)  # Start listening for interactions
    await view.wait() # Wait until the view times out or gets stopped
    await ctx.respond('時間到摟 小婊子')






def load(bot):
    bot.add_plugin(plugin)


def unload(bot):
    bot.remove_plugin(plugin)












