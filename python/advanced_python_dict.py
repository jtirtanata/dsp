import csv
import re
import common
import operator

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
print("Q6")
print(sorted(data.items())[:3])


with open(FILE, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for row in reader:
        match = re.match(r'(.*)\s([A-z]+)$', row[0])
        name = (match.group(1), match.group(2))
        title = common.fetch_title(row[2])
        data[name]= [row[1], title, row[3]]

print("Q7")
print(sorted(data.items(), key=lambda k: k[0][0])[:3])

print("Q8")
print(sorted(data.items(), key=lambda k: k[0][1]))
