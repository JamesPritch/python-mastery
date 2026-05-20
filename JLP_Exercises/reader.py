import csv
from typing import List, TextIO

def read_csv_as_dicts(filename:str, types:List[type]) -> List[dict]:
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types)

def read_csv_as_instances(filename:str, cls:type) -> List:
    '''
    Read CSV data into a list of instances
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls)

def csv_as_dicts(file:TextIO, types:List[type], headers:str = None) -> List[dict]:
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    records = []
    rows = csv.reader(file)
    if not headers:
        headers = next(rows)
    for row in rows:
        record = { name: func(val) 
                    for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(file:TextIO, cls:type, headers:str = None) -> List:
    '''
    Read CSV data into a list of instances
    '''
    records = []
    rows = csv.reader(file)
    if not headers:
        headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records
