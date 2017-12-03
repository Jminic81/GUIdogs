import csv
from sqlite3 import *

dataframe = connect('dogs89.db')
df = dataframe.cursor()
df.execute('CREATE TABLE Dog_Licc(Breed TEXT, Count INTEGER, Rank INTEGER)')
table = []
with open('Dogbreedsimport.csv', newline='') as f:
    reader = csv.reader(f)
    skip = next(reader)
    for row in reader:
        table.append(tuple(row))
print(table)
for line in table:
    df.execute('INSERT INTO dog_Licc VALUES (?, ?, ?)', line)
dataframe.commit()
