import csv
import numpy

def csv_reader(file_csv, col_num):
    reader = csv.reader(file_csv, delimiter=';')
    data = []
    for line in reader:
        data += [float(line[col_num - 1].replace(',', '.'))]
    return data

csv_path = "data.csv"
col_num = 1
with open(csv_path, encoding='utf-8', newline='') as f_obj:
    data = csv_reader(f_obj, col_num)

print('Среднее значение: ', numpy.mean(data))
print('Дисперсия: ', numpy.var(data))
print('Среднее квадратичное отклонение: ', numpy.std(data))
