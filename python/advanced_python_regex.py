# data: faculty.csv

# change to dir
import os
print(os.getcwd())

# read in file:
import csv
with open('faculty.csv', 'r') as f:
    data_list = list(csv.reader(f)) # cast reader object as list of lists
    header = data_list[0] # first row (list) is header 
    data = data_list[1:]
print(header) # ['name', ' degree', ' title', ' email']
print(data[0]) # ['Scarlett L. Bellamy', ' Sc.D.', 'Associate Professor of Biostatistics', 'bellamys@mail.med.upenn.edu']
print(len(data)) # 37 observations (excluding header)

# split dataset into separate variables (lists):
names = [row[0] for row in data]
degrees = [row[1] for row in data]
titles = [row[2] for row in data]
emails = [row[3] for row in data]

# check head and counts
print(names[:5])
print(degrees[:5]) # note: elements have leading whitespace
print(titles[:5])
print(emails[:5])

print(len(names)) # 37
print(len(degrees)) # 37
print(len(titles)) # 37
print(len(emails)) # 37

#### Q1: DEGREES AND FREQUENCIES

# return a list of strings with no leading whitespaces or punctuation
stripped_degrees = [degree.strip() for degree in degrees] # strip leading whitespace
np_degrees = [degree.replace(".","") for degree in stripped_degrees] # replace '.' with '', i.e. remove '.'
print(np_degrees)
print(len(np_degrees)) # 37

# check string lengths
from collections import Counter
lengths = [len(degree) for degree in np_degrees]
len_count = Counter(lengths)
print(len_count) # Counter({3: 32, 16: 1, 1: 1, 7: 1, 10: 1, 11: 1}) -> most strings have just 3 letters (e.g. PhD)

# split strings longer than 3 characters and add to a new expanded list
# exclude strings less than 2 characters
extended = []
for degree in np_degrees:
    if len(degree) < 2:
        np_degrees.pop()
    elif len(degree) > 3:
        tempdeg = degree.split()
        extended += tempdeg
    else: # len(degree) == 3
        extended.append(degree)
print(extended)
print(len(extended)) # 44

# print out counts

# print from Counter object:
deg_count = Counter(extended)
print(deg_count) # Counter({'PhD': 30, 'ScD': 6, 'MPH': 2, 'MS': 2, 'MD': 1, 'BSEd': 1, 'JD': 1, 'MA': 1})
for val, freq in deg_count.most_common():
    print('The number of {} degrees is {}'.format(val, freq))

# The number of PhD degrees is 30
# The number of ScD degrees is 6
# The number of MPH degrees is 2
# The number of MS degrees is 2
# The number of MD degrees is 1
# The number of BSEd degrees is 1
# The number of JD degrees is 1
# The number of MA degrees is 1

# print from dictionary:
deg_dict = dict(deg_count)
print(deg_dict) # {'MD': 1, 'PhD': 30, 'MS': 2, 'ScD': 6, 'MA': 1, 'BSEd': 1, 'MPH': 2, 'JD': 1}
for key in deg_dict:
    print('The number of {} degrees is {}'.format(key, deg_dict[key]))

# The number of MD degrees is 1
# The number of PhD degrees is 30
# The number of MS degrees is 2
# The number of ScD degrees is 6
# The number of MA degrees is 1
# The number of BSEd degrees is 1
# The number of MPH degrees is 2
# The number of JD degrees is 1


#### Q2: TITLE AND FREQUENCIES

# quick look
print(titles)
title_count = Counter(titles)
print(title_count)
# Counter({'Professor of Biostatistics': 13, 'Associate Professor of Biostatistics': 12,
# 'Assistant Professor of Biostatistics': 11, 'Assistant Professor is Biostatistics': 1})

# only 3 unique titles, fix one mistake ('of')
fixed_titles = [title.replace('is B', 'of B') for title in titles]
print(len(fixed_titles)) # 37
title_count = Counter(fixed_titles)
print(title_count)
# Counter({'Professor of Biostatistics': 13, 'Assistant Professor of Biostatistics': 12, 'Associate Professor of Biostatistics': 12})

# RESULT
for val, freq in title_count.most_common():
    print('The number of staff with the title {} is {}'.format(val, freq))

# The number of staff with the title Professor of Biostatistics is 13
# The number of staff with the title Assistant Professor of Biostatistics is 12
# The number of staff with the title Associate Professor of Biostatistics is 12

#### Q3: LIST OF EMAIL ADDRESSES

emails = [row[3] for row in data]

# RESULT
print(emails)

# ['bellamys@mail.med.upenn.edu', 'warren@upenn.edu', 'bryanma@upenn.edu', 'jinboche@upenn.edu', 'sellenbe@upenn.edu',
# 'jellenbe@mail.med.upenn.edu', 'ruifeng@upenn.edu', 'bcfrench@mail.med.upenn.edu', 'pgimotty@upenn.edu',
# 'wguo@mail.med.upenn.edu', 'hsu9@mail.med.upenn.edu', 'rhubb@mail.med.upenn.edu', 'whwang@mail.med.upenn.edu',
# 'mjoffe@mail.med.upenn.edu', 'jrlandis@mail.med.upenn.edu', 'liy3@email.chop.edu', 'mingyao@mail.med.upenn.edu',
# 'hongzhe@upenn.edu', 'rlocalio@upenn.edu', 'nanditam@mail.med.upenn.edu', 'knashawn@mail.med.upenn.edu',
# 'propert@mail.med.upenn.edu', 'mputt@mail.med.upenn.edu', 'sratclif@upenn.edu', 'michross@upenn.edu',
# 'jaroy@mail.med.upenn.edu', 'msammel@cceb.med.upenn.edu', 'shawp@upenn.edu', 'rshi@mail.med.upenn.edu',
# 'hshou@mail.med.upenn.edu', 'jshults@mail.med.upenn.edu', 'alisaste@mail.med.upenn.edu', 'atroxel@mail.med.upenn.edu',
# 'rxiao@mail.med.upenn.edu', 'sxie@mail.med.upenn.edu', 'dxie@upenn.edu', 'weiyang@mail.med.upenn.edu']

#### Q4: UNIQUE EMAIL DOMAINS

# split handle and domain with '@' as delimiter
split_emails = [email.split('@') for email in emails]
print(split_emails)

# construct new list of domains only
domains = [email[1] for email in split_emails]
print(domains)

# RESULT
unique_domains = list(set(domains))
print(unique_domains) # ['upenn.edu', 'cceb.med.upenn.edu', 'mail.med.upenn.edu', 'email.chop.edu']

