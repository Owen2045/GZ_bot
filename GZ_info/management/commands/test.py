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
    
    def tran_info(self, data):
        ud_info = ''
        if isinstance(data, str):
            str_list = data.split('\n')
            ud_list = []
            coup_list = []
            evurl_list = []
            coup_re = r'- \w{4}-\w{4}-\w{4}-\w{4}'

            for spec in str_list:
                if spec == '[COUPONS]':
                    coup_list.append('[優惠券]')
                elif re.match(coup_re, spec):
                    coup_list.append(spec)
                elif spec == '[EVENTS]':
                    evurl_list.append('[活動網址]')
                elif spec.startswith('- https:'):
                    evurl_list.append(spec)
                else:
                    ud_list.append(spec)

            translator = Translator()
            zh_obj_list = translator.translate(ud_list, dest='zh-tw')
            
            zh_list = [x.text for x in zh_obj_list if x]
            zh_list.extend(coup_list)
            zh_list.extend(evurl_list)
            ud_info = '\n'.join(zh_list)
        return ud_info

    def handle(self, *args, **options):
        qs = UpdateInfo.objects.filter(id=3)
        for i in qs:
            # print(i.info_time)
            print(i.update_info_zh)



