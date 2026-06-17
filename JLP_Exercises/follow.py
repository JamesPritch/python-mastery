import os
import time
from colorama import Fore

def follow(filename):
    f = open(filename)
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.01)
            continue
        yield line

for line in follow('../Data/stocklog.csv'):
    fields = line.split(',')
    name = fields[0].strip('"')
    price = float(fields[1])
    change = float(fields[4])
    if change < 0:
        print(Fore.RED + f'{name:>5}, {price: 7.2f}, {change: 6.2f}')
    else:
        print(Fore.GREEN + f'{name:>5}, {price: 7.2f}, {change: 6.2f}')
    print(Fore.WHITE + '', end = '')
