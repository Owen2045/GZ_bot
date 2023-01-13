import logging
import os
import re
import time
from datetime import date, datetime, timedelta
from dateutil import parser

import pandas as pd
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

from GZ_info.models import UpdateInfo
from GZ_info.util import time_proV2
from googletrans import Translator


logger = logging.getLogger('GZ_info')



class Command(BaseCommand):
    """
    解析+翻譯更新資訊
    """
    help = '解析+翻譯更新資訊'
    


    def handle(self, *args, **options):
        qs = UpdateInfo.objects.all().order_by('-id').values('info_time', 'info_time_str', 'update_info_en', 'update_info_zh', 'url')
        df = pd.DataFrame(qs, dtype=object)
        date_list = df['info_time_str'].tolist()


