import logging
import os
import re
import time
from datetime import date, datetime, timedelta
from dateutil import parser

import pandas as pd
from django.core.management.base import BaseCommand
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from GZ_info.models import UpdateInfo
from GZ_info.util import time_proV2


logger = logging.getLogger('GZ_info')



class Command(BaseCommand):
    """
    爬更新原文
    """
    help = '爬更新原文'
    
    def check_info(self):
        qs = UpdateInfo.objects.all().order_by('-info_time')
        exist_info = [x.info_time_str for x in qs[:5]]
        return exist_info

    def handle(self, *args, **options):
        
        exist_info = self.check_info()
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--headless")
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        browser.get('https://gamezbd-info.pages.dev/info')
        try:
            element = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'text-secondary')))
        except:
            element = None
            logger.warning('get info element fail!')

        if element:
            bb = browser.find_elements(By.CLASS_NAME, 'text-secondary')
            data_list = []
            for i in bb:
                result = {}
                title = i.text
                if 'Update' in title:        
                    ud_str = title.split('\n')
                    if len(ud_str) < 0:
                        continue
                    ud_time = ud_str[0]
                    ud_time_og = re.search(r"(\d{1,2}/\d{1,2}/\d{4})", ud_time).group(0)
                    try:
                        ud_time_fm = datetime.strptime(ud_time_og, "%m/%d/%Y").strftime('%Y-%m-%d')
                        ud_time_dt = time_proV2(ud_time_fm)
                        if ud_time_fm in exist_info:
                            continue
                    except Exception as e:
                        continue

                url = i.get_attribute('href')
                if isinstance(url, str):
                    if 'update' in url:
                        result['info_time_str'] = ud_time_fm
                        result['info_time'] = ud_time_dt
                        result['url'] = url
                if result:
                    data_list.append(result)

            if data_list:
                df = pd.DataFrame(data_list)
                df = df[~df['info_time_str'].isin(exist_info)]
                df = df.sort_values('info_time_str')                
                df = df[['info_time', 'info_time_str', 'url']].to_dict(orient='records')
                entry_data = [UpdateInfo(**x) for x in df]
                if entry_data:
                    UpdateInfo.objects.bulk_create(entry_data)
                    logger.info(f'info 寫入完成: {len(entry_data)} 筆')











