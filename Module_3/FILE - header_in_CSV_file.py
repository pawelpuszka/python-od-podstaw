import csv

with open('test_files/server_logs.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)  # jeżeli w pliku podany nagłówek to staje się inexem

    for row in csv_reader:
        print(row['status_code'])