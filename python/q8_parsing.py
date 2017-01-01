# The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.
import csv
import math
FOOTBALL_FILE = 'football.csv'
difference = []

with open(FOOTBALL_FILE, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        goalsFor = int(row['Goals'])
        goalsAgainst = int(row['Goals Allowed'])
        difference.append((row['Team'], math.fabs(goalsFor - goalsAgainst)))

print(sorted(difference, key=lambda x: x[1])[0][0])
