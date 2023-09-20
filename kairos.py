import csv
import random as r

header = ['id', 'age', 'gender', 'neighbourhood', 'occupation', 'opinion']
data=[]

genders=["M", "M", "F", "F", "NB", "X"]
occupations=["S","E","C"]
opinions=["Y", "Y", "N", "N", "B"]

for i in range (200):
    arr=[i, r.randint(18,80), r.choice(genders), r.randint(1,9), r.choice(occupations), r.choice(opinions)]
    data.append(arr)

with open('fakedata.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)
