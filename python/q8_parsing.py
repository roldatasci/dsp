# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import os

print(os.getcwd())
os.chdir('metisgh/prework/dsp/python')  # change to directory with script and data
print(os.getcwd())

import csv

f = open('football.csv', 'r')
data_list = list(csv.reader(f))
header = data_list[0]  # isolate header
data = data_list[1:]  # rows of data (no header)
print(header)  # ['Team', 'Games', 'Wins', 'Losses', 'Draws', 'Goals', 'Goals Allowed', 'Points']
print(data[0])  # first row = ['Arsenal', '38', '26', '9', '3', '79', '36', '87']

# idx 5 is goals
# idx 6 is goals allowed

def smallest_diff(data):
    teams = [row[0] for row in data]
    diffs = [abs(int(row[5]) - int(row[6])) for row in data]
    team_diffs = list(zip(diffs, teams))
    team_diffs.sort() # sorting in place
    return team_diffs[0][1] # return first tuple's second element

print(smallest_diff(data)) # Aston_Villa