import csv

INPUT_FILE = 'faculty.csv'
OUTPUT_FILE = 'emails.csv'
with open(INPUT_FILE, 'r') as infile, open(OUTPUT_FILE, 'w') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    next(reader, None)
    for row in reader:
        writer.writerow([row[3]])
