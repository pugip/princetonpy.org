import datetime
from datetime import date, timedelta


def first_monday_of_month(month, year) -> date:
    day1 = date(year, month, 1)
    day1_wkday = day1.weekday()
    return day1 if day1_wkday == 0 else day1 + timedelta(7 - day1_wkday)


def next_second_monday(today=None):
    """
    # later this month
    >>> next_second_monday(date(2021, 9, 1))
    datetime.date(2021, 9, 13)

    # today!
    >>> next_second_monday(date(2021, 9, 13))
    datetime.date(2021, 9, 13)

    # next month
    >>> next_second_monday(date(2021, 9, 19))
    datetime.date(2021, 10, 11)

    # next year
    >>> next_second_monday(date(2021, 12, 29))
    datetime.date(2022, 1, 10)
    """
    if today is None:
        today = date.today()

    second_monday_this_month = first_monday_of_month(
        today.month, today.year
    ) + timedelta(7)
    if second_monday_this_month < today:
        next_month = (1 + today.month) if today.month < 12 else 1
        year_of_next_month = today.year if today.month < 12 else 1 + today.year
        second_monday_of_next_month = first_monday_of_month(
            next_month, year_of_next_month
        ) + timedelta(7)
        result = second_monday_of_next_month
    else:
        result = second_monday_this_month
    # convert to date if it's a datetime.
    return getattr(result, "date", result)


def get_next_meeting_time(t: datetime.time = datetime.time(19, 0)) -> datetime.datetime:
    d = next_second_monday()
    return datetime.datetime.combine(d, t)


def make_ordinal(n):
    """
    Convert an integer into its ordinal representation::
    >>> make_ordinal(0)
    '0th'
    >>> make_ordinal(3)
    '3rd'
    >>> make_ordinal(122)
    '122nd'
    >>> make_ordinal(213)
    '213th'
    """
    n = int(n)
    if 11 <= (n % 100) <= 13:
        suffix = "th"
    else:
        suffix = ["th", "st", "nd", "rd", "th"][min(n % 10, 4)]
    return str(n) + suffix


def make_time(t: datetime.time) -> str:
    """
    Convert a time into a readable format::
    >>> make_time(datetime.time(9, 0))
    '9AM'
    >>> make_time(datetime.time(12, 30))
    '12:30PM'
    """
    if t.minute == 0:
        return f'{t.strftime("%-I")}{t.strftime("%p").lower()}'
    return f'{t.strftime("%-I:%M")}{t.strftime("%p").lower()}'


def make_when(dt: datetime.datetime, with_time: bool = True) -> str:
    """
    Convert a datetime into a readable format::
    >>> make_when(datetime.datetime(2021, 9, 1))
    'Wednesday, November 1st @ 12AM'
    >>> make_when(datetime.datetime(2021, 9, 1), with_time=False)
    'Wednesday, November 1st'
    """
    if with_time:
        return (
            f'{dt.strftime("%A, %B")} {make_ordinal(dt.day)} @ {make_time(dt.time())}'
        )
    return f'{dt.strftime("%A, %B")} {make_ordinal(dt.day)}'
