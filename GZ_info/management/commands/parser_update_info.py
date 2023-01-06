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
    

    def crawling_data(self, url):
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        reds = soup.find_all('div', class_='bbCodeBlock bbCodeCode')
        patch_str = reds[0].pre.text        
        return patch_str

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
        qs = UpdateInfo.objects.filter(is_complete=0)
        if not qs:
            logger.info('不須更新')
            return

        for i in qs:
            url = i.url
            ud_info_en = self.crawling_data(url=url)
            ud_info_zh = self.tran_info(data=ud_info_en)
            i.update_info_en = ud_info_en
            i.update_info_zh = ud_info_zh
            i.is_complete = True
            logger.info(f'{i.info_time_str} 更新完成')
            time.sleep(1)
        UpdateInfo.objects.bulk_update(qs, fields=['update_info_en', 'update_info_zh', 'is_complete'])
        logger.info('更新完成')







