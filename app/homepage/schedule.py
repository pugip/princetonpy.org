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

    second_monday_this_month = first_monday_of_month(today.month, today.year) + timedelta(7)
    if second_monday_this_month < today:
        next_month = (1 + today.month) if today.month < 12 else 1
        year_of_next_month = today.year if today.month < 12 else 1 + today.year
        second_monday_of_next_month = first_monday_of_month(next_month, year_of_next_month) + timedelta(7)
        result = second_monday_of_next_month
    else:
        result = second_monday_this_month
    # convert to date if it's a datetime.
    return getattr(result, 'date', result)

