import datetime

print(datetime.datetime.now())
print(datetime.date.today())
print(datetime.datetime.fromtimestamp(1724101323))

# odejmowanie dat
date1 = datetime.datetime(2024, 8, 19)
date2 = datetime.datetime(2024, 9, 10)
print(date2 - date1)

# odejmowanie  dni od określonej daty
date1 += datetime.timedelta(10)  # argumentem jest liczba dni
print(date1)




