from datetime import datetime, timedelta, date

# print(datetime.now())
# print(date.today())
# print(datetime.fromtimestamp(1724101323))

# odejmowanie dat
date1 = datetime(2024, 8, 19)
date2 = datetime(2024, 9, 10)
# print(date2 - date1)

# odejmowanie  dni od określonej daty
date1 += timedelta(10)  # argumentem jest liczba dni
# print(date1)

# zmiana daty na tekst
now = datetime.now()
# print(now)

now_str = now.strftime("%Y-%m-%d %H:%M:%S")
# print(now_str)


# zmiana tekstu na datę
date_str = '20.08.2024 22:33:15'
date = datetime.strptime(date_str, "%d.%m.%Y %H:%M:%S")
# print(date)



import locale

date_str = '20 August 2024'
date = datetime.strptime(date_str, "%d %B %Y")
# print(date)

locale.setlocale(locale.LC_TIME, "szl_PL")
date_str = '20 kwietnia 2024'
date = datetime.strptime(date_str, "%d %B %Y")
# print(date)


#  obliczanie długości wykonywania programu

import time

start_time = time.time()

for _ in range(100000000):
    pass

end_time = time.time()

print(end_time - start_time)
