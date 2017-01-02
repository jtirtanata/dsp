import csv
import re
import common

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

def title_counter(full_title):
    title = common.fetch_title(full_title)
    frequency_counter(title_frequency, title)

def email_counter(email):
    email_list.append(email)
    match = re.fullmatch(r'[\w_\-\.]+@([\w\.]+)', email)
    frequency_counter(domain_frequency, match.group(1))

def print_frequency_dict(d):
    for k,v in d.items():
        print ('- {} : {}'.format(k, v))

with open(FILE, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for row in reader:
        degree_counter(row[1])
        title_counter(row[2])
        email_counter(row[3])

print('There are {} different degrees.'.format(len(degree_frequency)))
print_frequency_dict(degree_frequency)
print('There are {} different titles.'.format(len(title_frequency)))
print_frequency_dict(title_frequency)
print('List of emails:')
for email in email_list:
    print('- {}'.format(email))
print('There are {} different domains.'.format(len(domain_frequency)))
print_frequency_dict(domain_frequency)
