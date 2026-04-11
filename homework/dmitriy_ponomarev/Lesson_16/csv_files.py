import csv

with open('data.csv', newline='') as csv_file:
    file_data = csv.reader(csv_file)
    data = []
    for row in file_data:
        data.append(row)

# print(data)
for name, last_name, city in data:
    print(f'Name: {name}, last_name: {last_name}, city: {city}')
    

with open('data.csv', newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    data = []
    for row in file_data:
        data.append(row)

for row in data:
    print(row)
