from datetime import datetime, timedelta, date

def number_of_days_between(date1s: str(), date2s: str()) -> int():
    date1 = datetime.strptime(date1s, "%Y-%m-%d")
    date2 = datetime.strptime(date2s, "%Y-%m-%d")
    diff = date1 - date2
    return diff


print(number_of_days_between('2024-09-06', '2023-09-06'))