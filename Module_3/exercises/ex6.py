# 6.Napisz program, który zamienia podany tekst w formacie “DD-MM-YYYY” na obiekt datetime i wypisuje go w formacie “YYYY/MM/DD”.
from datetime import datetime
def converse_date(date_str: str()):
    date = datetime.strptime(date_str, "%d-%m-%Y")
    date = datetime.strftime(date, "%Y/%m/%d")

    print(date)



converse_date('04-09-2024')