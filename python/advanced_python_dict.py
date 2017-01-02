import csv
import re
import common

FILE = 'faculty.csv'

data = {}

def last_name(name):
    match = re.match(r'.*\s([A-z]+)$', name)
    return match.group(1)

with open(FILE, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for row in reader:
        lastname = last_name(row[0])
        if lastname not in data:
            data[lastname] = []
        title = common.fetch_title(row[2])
        data[lastname].append([row[1], title, row[3]])
print("Unordered data:")
first_three_keys = list(data.keys())[:3]
for key in first_three_keys:
    print('{}: {}'.format(key, data[key]))


print("Ordered data:")
ordered_keys = sorted(list(data.keys()))
for key in ordered_keys:
    print('{}: {}'.format(key, data[key]))
