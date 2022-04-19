import pandas as pd
import numpy as np
import math
from datetime import datetime, timedelta


def busday_count( date_start, date_end, holidays=None, weekmask=None):
    """
    Return the number of business days, excluding holidays
    """
    all_date_holidays = []
    date_range = pd.date_range(date_start, date_end).strftime('%Y-%m-%d')
    all_date_holidays.extend(date_range)
    data_date = {}
    all_date_holidays = list(filter(lambda x: x not in holidays, all_date_holidays))
    for date in all_date_holidays:
        data_date[date] = pd.to_datetime(date).weekday()
    number_day = 0
    for key, value in data_date.items():
        number_day += weekmask[value]
    return number_day

date_start = datetime.strptime('2022-04-27', '%Y-%m-%d').date()
date_end = datetime.strptime('2022-04-27', '%Y-%m-%d').date()
week_mask = [1, 1, 1, 1, 1, 0, 0]
holidays = ['2022-04-25', '2022-04-26']
number_day = busday_count(date_start, date_end, holidays=holidays, weekmask=week_mask)
print(number_day)