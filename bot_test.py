import os
import requests
import time
from urllib import request
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE',  'GZ_bot.settings')




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument("--headless")
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

browser.get('https://gamezbd-info.pages.dev/info')
try:
    element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'text-secondary')))
except:
    pass
bb = browser.find_elements(By.CLASS_NAME, 'text-secondary')
if element:
    update_url = []
    # time.sleep(50)
    for i in bb:
        title = i.text
        url = i.get_attribute('href')
        if isinstance(url, str):
            if 'update' in url:
                print(url)
                update_url.append(url)
    print(update_url)
