import csv
import collections
from sys import intern
from abc import ABC, abstractmethod


# Classes
class DataCollection(collections.abc.Sequence):
    def __init__(self):
        kwargs = collections.defaultdict()
        for cols in headers:
            kwargs[cols] = []
        self.__dict__.update(kwargs)
    def __len__(self):
        return len(self.__dict__[headers[0]]) # Assume all lists have equal lengths
    def __getitem__(self, index):
        if isinstance(index, int):
            return {str(col):self.__dict__[cols][index] for col, cols in zip(header, headers)}
        listofsets = DataCollection()
        for i in range(index.start, index.stop):
            listofsets.append({cols: self.__dict__[cols][i] for cols in headers})
        return listofsets
    def append(self, d): 
        for cols in headers:
            self.__dict__[cols].append(d[cols])

class CSVParser(ABC):
    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records
    
    @abstractmethod
    def make_record(self, headers, row):
        pass

class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types
    def make_record(self, headers, row):
        return { name: func(val) for name, func, val in zip(headers, self.types, row) }
    
class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls
    def make_record(self, headers, row):
        return self.cls.from_row(row)


# Functions
# Reads a csv file and converts the types of its columns 
def read_csv_as_dicts(filename, coltypes):
    parser = DictCSVParser(coltypes)
    return parser.parse(filename)


def read_csv_as_columns(filename, coltypes=[str, str, str, int]):
    '''
    Read any csv file with headers in the first row and save them as lists
    '''
    with open(filename) as f:
        global header
        global headers
        rows = csv.reader(f)
        # Assuming headers from the first row
        header = next(rows)
        # Turn headers plural, i.e. route -> routes, rides -> numrides
        headers = ['num' + col if col[-1] == 's' else col + 's' for col in header]
        records = DataCollection()
        for row in rows:
            record = {cols:func(val) for cols, func, val in zip(headers, coltypes, row)}
            records.append(record)
    return records

def read_csv_as_instances(filename, cls):
    parser = InstanceCSVParser(cls)
    return parser.parse(filename)