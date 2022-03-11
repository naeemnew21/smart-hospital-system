
from datetime import datetime, timedelta




def arrange():
    n    = datetime.today().weekday()
    days =["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    return days[n:]+days[:n]


def arrange_dates(day_list):
    dic = {}
    today = datetime.today().date()
    for i,day in zip(range(7), arrange()):
        next_day = today + timedelta(days=i)
        if day in day_list:
            dic[day] = next_day
    return dic



def get_date(day_name):
    today = datetime.today().date()
    for i,day in zip(range(7), arrange()):
        next_day = today + timedelta(days=i)
        if day_name == day:
            return next_day

