import os
import requests

from urllib import request
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE',  'GZ_bot.settings')





url = 'https://gamezbd-info.pages.dev/timer'
request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
webpage = urlopen(request_site).read()
soup = BeautifulSoup(webpage, "html.parser")
mydivs = soup.find(id_='q-app')
print(mydivs)

