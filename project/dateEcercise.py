import datetime


# if month is december, so next month
def month_december(month):
    if month > 12:
        return month - 12
    else:
        return month


# if month is december, so next year
def year_december(year, month):
    if month > 12:
        return year + 1
    else:
        return year


# validation
def days_in_month(year, month):
    if (month < 1) or (month > 12):
        print("please enter a valid month")
    elif (year < 1) or (year > 9999):
        print("please enter a valid year between 1 - 9999")
    else:
        # subtract current month from next month then get days
        days = (datetime.date(year_december(year, month + 1), month_december(month + 1), 1) - datetime.date(year,
                                                                                                            month,
                                                                                                            1)).days

        date = datetime.datetime(year, month, days)
        res = str(date) + '  ' + date.strftime("%A")
        return res


print(days_in_month(1996, 9))