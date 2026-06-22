from follow import *

# Garbage collection of running generator
f = follow('../Data/stocklog.csv')
next(f)
del f

# Closing a generator
f = follow('../Data/stocklog.csv')
for line in f:
    print(line, end = '')
    if 'IBM' in line:
        f.close()

# Generator is done
for line in f:
    print(line, end='')

# This can be run multiple times
f = follow('../Data/stocklog.csv')
for line in f:
    print(line, end='')
    if 'IBM' in line:
        break

del f

# Throwing errors
from cofollow import printer
p = printer()
p.send('hello') # hello
p.send(42) # 42
p.throw(ValueError('It failed')) # ERROR: ValueError('It failed',)
try:
    int('n/a')
except Exception as e:
    p.throw(e) # ERROR: ValueError("invalid literal for int() with base 10: 'n/a'",)
