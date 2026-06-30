import csv
import logging
log = logging.getLogger(__name__)

def read_csv_as_dicts(filename, types, *, headers = None):
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types, headers = headers)

def read_csv_as_instances(filename, cls, *, headers = None):
    '''
    Read CSV data into a list of instances
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls, headers = headers)

def csv_as_dicts(lines, types, *, headers = None):
    '''
    Convert CSV data into a list of dictionaries with optional type conversion
    '''
    return convert_csv(lines, 
                       lambda headers, row: {name: func(val) for name, func, val 
                                             in zip(headers, types, row)}, 
                       headers = headers)

def csv_as_instances(lines, cls, *, headers = None):
    '''
    Convert CSV data into a list of instances
    '''
    return convert_csv(lines, 
                       lambda headers, row: cls.from_row(row), 
                       headers = headers)

def convert_csv(lines, converter, *, headers = None):
    '''
    Convert CSV data into some user defined format
    '''
    rows = csv.reader(lines)
    results = []
    if not headers:
        headers = next(rows)
    for index, row in enumerate(rows):
        try:
            result = converter(headers, row)
            results.append(result)
        except ValueError as e:
            log.warning(f'Row {index+1}: bad row {row}')
            log.debug(f'Reason: {e}')
    return results

def make_dict(headers, row):
    return dict(zip(headers, row))
