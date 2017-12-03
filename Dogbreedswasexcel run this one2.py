import csv
from sqlite3 import *

dataframe = connect('Dogs17.db')
df = dataframe.cursor()
df.execute('CREATE TABLE Dog_Rank(Breed TEXT, Count INTEGER, Rank INTEGER)')
table = []
with open('Dogbreedsimport.csv', newline='') as f:
    reader = csv.reader(f)
    skip = next(reader)
    for row in reader:
        table.append(tuple(row))
print(table)
for line in table:
    df.execute('INSERT INTO Dog_Rank VALUES (?, ?, ?)', line)
dataframe.commit()
