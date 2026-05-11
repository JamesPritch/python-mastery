import csv
import collections

# Columns 
class RideData(collections.abc.Sequence):
    def __init__(self):
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []
    def __len__(self):
        return len(self.routes) # Assume all lists have equal lengths
    def __getitem__(self, index):
        if isinstance(index, int):
            return { 'route': self.routes[index],
                    'date': self.dates[index],
                    'daytype': self.daytypes[index],
                    'rides': self.numrides[index] }
        # Assuming index of 0:x type
        x = len(self.routes[index])
        listofsets = RideData()
        for i in range(x):
            listofsets.append({
                'route': self.routes[i], 
                'date': self.dates[i],
                'daytype': self.daytypes[i],
                'rides': self.numrides[i]
            })
        return listofsets
    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])


# Tuples
def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

# Dictionaries
def read_rides_as_dictionaries(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides,
            }  
            records.append(record)
    return records

# Classes
# instance = 'classes'
# class Row:
#     def __init__(self, route, date, daytype, rides):
#         self.route = route
#         self.date = date
#         self.daytype = daytype
#         self.rides = rides

# # Named tuples
# instance='named tuples'
# from collections import namedtuple
# Row = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])

# Classes with slots
instance = 'classes with slots'
class Row:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

def read_rides_as_instances(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records

# Classes
def read_rides_as_columns(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)

# Main
if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_rides_as_tuples('/data/home/james.pritchard/Python_mastery/Data/ctabus.csv')
    print('Memory Use for tuples: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    rows = read_rides_as_dictionaries('/data/home/james.pritchard/Python_mastery/Data/ctabus.csv')
    print('Memory Use for dictionaries: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    rows = read_rides_as_instances('/data/home/james.pritchard/Python_mastery/Data/ctabus.csv')
    print('Memory Use for '+str(instance)+': Current %d, Peak %d' % tracemalloc.get_traced_memory())