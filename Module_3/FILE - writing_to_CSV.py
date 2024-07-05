import csv

# with open('test_files/users.csv', 'w') as csv_file:
    # csv_writer = csv.writer(csv_file)  # obiekt służący do zapisywania danych w pliku CSV

    # csv_writer.writerow(['Pawel', 42])
    # csv_writer.writerow(['Ania', 25])

with open('test_files/users.csv', 'w') as csv_file:
    fieldnames = ['name', 'age']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    csv_writer.writeheader()
    csv_writer.writerow(
        {
            'name': 'Adam'
            ,'age': 42
        }
    )


