import collections
import csv
import functools
import json
import re
import sys
import time
from datetime import date, datetime, timedelta, tzinfo

import pandas as pd
import pytz
from dateutil import parser
from django.conf import settings

tz = pytz.timezone(settings.TIME_ZONE)


def time_proV2(time_data=None, plus_8=False):
    format_time = None
    if time_data:
        if isinstance(time_data, datetime):
            format_time = time_data  
            format_time = format_time.astimezone(tz)
        elif isinstance(time_data, date):
            format_time = datetime.combine(time_data, datetime.min.time()).astimezone(tz)
        elif isinstance(time_data, str):
            try:
                time_data = parser.parse(time_data).replace(tzinfo=None)
                format_time = time_data   
                format_time = format_time.astimezone(tz)
            except:
                pass
        else:
            try:
                format_time = str(time_data)
                format_time = parser.parse(format_time).replace(tzinfo=None)
                format_time = format_time.astimezone(tz)
            except Exception as e:
                pass
    if plus_8 == True and format_time:
        format_time = format_time + timedelta(hours=8)
    return format_time
