import json

try:
    with open('MOCK_DATA.json') as file_open:
        data = json.load(file_open)
except FileNotFoundError as e:
    print('File not found')

try:
    with open('MOCK_DATA.json') as file_open:
        data = json.load(file_open)
except IOError as e:
    print('Problem with input or output')

try:
    with open('MOCK_DATA.json') as file_open:
        data = json.load(file_open)
except NameError as e:
    print('Name not found')


def json_read(name_file):
    with open(name_file) as file_open:
        data = json.load(file_open)

    t = []
    title = '| {:^3}| {:^10}| {:^13}| {:^30}| {:^6}| {:^15}|'.format('ID','First name','Last name','Email','Gender','IP-address')
    delimiter = '-'*len(title)
    val = '| {id:<3}| {first_name:10}| {last_name:13}| {email:30}| {gender:6}| {ip_address:15}|'
    t.append(delimiter)
    t.append(title)
    t.append(delimiter)
    for i in range(len(data)):
        tmp = data[i]
        res = val.format(**tmp)
        t.append(res)
        t.append(delimiter)
    return t


file_name = json_read('MOCK_DATA.json')
for i in file_name:
    print(i)
