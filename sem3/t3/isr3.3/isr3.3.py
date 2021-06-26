import json
with open('file.json', 'r', encoding='utf-8') as f:
     data = json.load(f)

import csv
with open('finish.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)