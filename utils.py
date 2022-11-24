from datetime import datetime


def advent():
    date_now = datetime.now()
    date_stop = datetime(2023, 1, 1)
    days_left = date_stop - date_now
    return f'До Нового Года осталось {days_left.days} дней!'


