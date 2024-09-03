# 4.Napisz program, który odczytuje zawartość pliku tekstowego i wypisuje ją na ekran.

test_file = '../test_files/test.txt'

with open(test_file, encoding='utf-8') as file:
    file_content = file.read()

print(file_content)

import csv
log_file = '../test_files/server_logs.csv'
with open(log_file) as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        print(row)



import json
phone_file = '../phone-shop/phones.json'
with open(phone_file) as file:
    phones = json.load(file)

    for phone in phones:
        print(phone)
        
    print(phones[0]['specifications']['color'])