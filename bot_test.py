import os
import requests

from urllib import request
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE',  'GZ_bot.settings')




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
browser.get('https://gamezbd-info.pages.dev/timer')
div3 = browser.find_element(By.XPATH,'//*[@id="q-app"]/div/div[2]/div[1]/main/div/div[2]/div')
print(div3.text)

