import csv

with open('test_files/server_logs.csv') as csv_file:
    csv_reader = csv.reader(csv_file)  # zwraca obiekt iterator
    # csv_reader = csv.reader(csv_file, delimiter=';')  # wskazanie separatora innego niż domyslny

    for row in csv_reader:
        print(row[0])