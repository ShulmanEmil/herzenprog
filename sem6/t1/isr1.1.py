import csv
from math import sqrt

def mean_quadratic_deviation(data):
    m_q_deviation = sqrt(dispersion(data))
    return m_q_deviation

def dispersion(data):
    data_average = average(data)
    data_for_dispersion = [(x_i - data_average) ** 2 for x_i in data]
    sum_data = sum(data_for_dispersion)
    data_dispersion = sum_data/(len(data_for_dispersion))
    return data_dispersion

def average(data):
    sum_data = sum(data)
    count_data = len(data)
    data_average = sum_data/count_data
    return data_average

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

print('Среднее значение: ', average(data))
print('Дисперсия: ', dispersion(data))
print('Среднее квадратичное отклонение: ', mean_quadratic_deviation(data))
    
