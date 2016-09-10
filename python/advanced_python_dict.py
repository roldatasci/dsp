# DICTIONARIES

#### Q6: CREATE A DICTIONARY IN BELOW FORMAT

# {'surname': [['degree', 'title', 'email']]}

# read in file
import csv
with open('faculty.csv', 'r') as f:
    data_list = list(csv.reader(f)) # cast reader object as list of lists
    header = data_list[0] # first row (list) is header
    data = data_list[1:]
print(header) # ['name', ' degree', ' title', ' email']
print(data[0]) # ['Scarlett L. Bellamy', ' Sc.D.', 'Associate Professor of Biostatistics', 'bellamys@mail.med.upenn.edu']
print(len(data)) # 37 observations (excluding header)

# split dataset into separate variables (lists) to inspect:
names = [row[0] for row in data]
degrees = [row[1] for row in data] # note: leading white space
titles = [row[2] for row in data] # note: mistake on one title
emails = [row[3] for row in data]

# remove leading whitespace from degrees
degrees = [row[1].strip() for row in data]
print(degrees)

# redo titles
titles = [row[2].replace('is B', 'of B') for row in data]
titles = [row[2].replace(' of Biostatistics', '') for row in data]
print(titles)

# construct values
values = list(zip(degrees, titles, emails))
values = [list(value) for value in values]

# construct keys
# split 'name' string (on whitespace delimiter) into a list of strings and index the last element to get surname
surnames = [row[0].split(' ')[-1] for row in data]

# construct key:value pairs and pass to dict() constructor
pairs = list(zip(surnames, values))
d1 = dict(pairs)
print(d1)
for key, value in d1.items():
    print(key, value)

#### Q7: CREATE A NEW DICTIONARY WITH THE FOLLOWING FORMAT

# {('firstname', 'lastname'): ['degree', 'title']}

# reformat keys
firstnames = [row[0].split(' ')[0] for row in data]
lastnames = [row[0].split(' ')[-1] for row in data]
keys2 = list(zip(firstnames, lastnames))

# construct key:value pairs and pass to dict() constructor
pairs2 = list(zip(keys2, values))
d2 = dict(pairs2)
print(d2)
for key, value in d2.items():
	print(key, value)


#### Q8: CREATE A NEW DICTIONARY WITH KEYS BY LAST NAME AND PRINT OUT PAIRS ORDERED BY LAST NAME

# reformat keys
keys3 = list(zip(lastnames, firstnames))
print(keys3)

pairs3 = list(zip(keys3, values))
d3 = dict(pairs3)
print(d3)
for key, value in sorted(d3.items()):
    print(key, value)