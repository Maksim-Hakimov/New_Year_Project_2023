import datetime


def advent():
    now = datetime.datetime.today()
    new_year = datetime.datetime(2023, 1, 1)
    d = new_year - now

    mm, ss = divmod(d.seconds, 60)
    hh, mm = divmod(mm, 60)

    time = f'До нового года: {d.days} дней {hh} часа {mm} мин {ss} сек.'

    return time
