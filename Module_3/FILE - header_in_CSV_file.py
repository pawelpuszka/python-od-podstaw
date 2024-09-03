import csv

with open('test_files/server_logs.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)  # jeżeli w pliku podany nagłówek to jego elementy stają się indexem dla całej kolumny

    for row in csv_reader:
        print(row['status_code'])