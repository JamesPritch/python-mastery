def frange(start, stop, step):
    while start < stop:
        yield start
        start += step

f = frange(0, 2, 0.25)
for x in f:
    print(x, end = ' ') # Outputs 0 0.25 0.5 0.75 1.0 1.25 1.5 1.75

for x in f:
    print(x, end = ' ') # Outputs 

class FRange:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
    def __iter__(self):
        n = self.start
        while n < self.stop:
            yield n
            n += self.step
