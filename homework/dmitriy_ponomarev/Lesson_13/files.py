import os

# data_file = open('data.txt', 'r')
# data_file.read()
# print('asdasdas' + 1)
# data_file.close()

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'data.txt')
new_file_path = os.path.join(base_path, 'data2.txt')
print(file_path)

def read_file():
    with open(file_path, 'r') as data_file:
        for line in data_file.readlines():
            yield line

for data_line in read_file():
    with open(new_file_path, 'a') as new_file:
        data_line = data_line.replace('.', '').replace(',', '')
        new_file.write(data_line)

homework_path = os.path.dirname(os.path.dirname(base_path))
dmitro_file_path = os.path.join(homework_path, 'dmitro_p', 'dmitro.txt')
print(dmitro_file_path)

with open(dmitro_file_path) as dmitro_file:
    print(dmitro_file.read())