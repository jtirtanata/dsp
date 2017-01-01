import csv
import re
FILE = 'faculty.csv'

degree_frequency = {}
title_frequency = {}
email_list = []
domain_frequency = {}

def frequency_counter(frequencyDict, value):
    if value in frequencyDict:
        frequencyDict[value] += 1
    else:
        frequencyDict[value] = 1

def degree_counter(degrees):
    if degrees == '0':
        return
    degrees = degrees.split()
    for degree in degrees:
        degree = degree.replace('.','')
        frequency_counter(degree_frequency, degree)

def title_counter(title):
    match = re.fullmatch(r'([A-Z][\w-]*(\s+[A-Z][\w-]*)*)\s+(\w){2}\s+(Biostatistics)', title)
    frequency_counter(title_frequency, match.group(1))

def email_counter(email):
    email_list.append(email)
    match = re.fullmatch(r'[\w_\-\.]+@([\w\.]+)', email)
    frequency_counter(domain_frequency, match.group(1))


with open(FILE, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for row in reader:
        degree_counter(row[1])
        title_counter(row[2])
        email_counter(row[3])

def print_frequency_dict(d):
    for k,v in d.items():
        print ('- {} : {}'.format(k, v))


print('There are {} different degrees.'.format(len(degree_frequency)))
print_frequency_dict(degree_frequency)
print('There are {} different titles.'.format(len(title_frequency)))
print_frequency_dict(title_frequency)
print('List of emails:')
for email in email_list:
    print('- {}'.format(email))
print('There are {} different domains.'.format(len(domain_frequency)))
print_frequency_dict(domain_frequency)
