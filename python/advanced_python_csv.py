# WRITING TO CSV

# change to dir
import os
print(os.getcwd())

# read in input file
import csv
with open('faculty.csv', 'r') as f:
    data_list = list(csv.reader(f))
    header = data_list[0]
    data = data_list[1:]
print(header) # ['name', ' degree', ' title', ' email']
print(data[0]) # ['Scarlett L. Bellamy', ' Sc.D.', 'Associate Professor of Biostatistics', 'bellamys@mail.med.upenn.edu']
print(len(data)) # 37 observations (excluding header)

# emails
emails = [row[3] for row in data]
print(emails)

# write result to 'emails.csv' (import csv)
with open('emails.csv', 'wb') as fout:
    csvwriter = csv.writer(fout) # creater writer object
    for email in emails:
        csvwriter.writerow([email])

