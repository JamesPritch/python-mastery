from follow import follow
import csv
lines = follow('../Data/stocklog.csv')
rows = csv.reader(lines)
for row in rows:
    print(row)
