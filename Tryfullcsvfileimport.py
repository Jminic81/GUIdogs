import csv
from sqlite3 import *

dataframe = connect('dogs90.db')
df = dataframe.cursor()
df.execute('CREATE TABLE All_Dogs(LicenseType TEXT, Breed TEXT, Color TEXT, DogName TEXT, OwnerZip INTEGER, ExpYear INTEGER)')
table = []
with open('Alldogs2017.csv', newline='') as f:
    reader = csv.reader(f)
    skip = next(reader)
    for row in reader:
        table.append(tuple(row))
print(table)
for line in table:
    df.execute('INSERT INTO All_Dogs VALUES (?, ?, ?, ?, ?, ?)', line)
dataframe.commit()
