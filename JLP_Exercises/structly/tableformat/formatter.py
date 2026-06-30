from abc import ABC, abstractmethod
__all__ = ['create_formatter', 'print_table']

# Classes
class TableFormatter(ABC):
    _formats = {}

    @classmethod
    def __init_subclass__(cls):
        name = cls.__module__.split('.')[-1]
        TableFormatter._formats[name] = cls

    @abstractmethod
    def headings(self, headers):
        pass
    @abstractmethod
    def row(self, rowdata):
        pass

class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)

class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])

# Functions
def print_table(data, fields, formatter):
    # if not isinstance(data, TableFormatter):
    #     raise TypeError('Expected a TableFormatter')
    formatter.headings(fields)
    for s in data:
        rowdata = [getattr(s, fieldname) for fieldname in fields]
        formatter.row(rowdata)

def create_formatter(type, column_formats = False, upper_headers = False):
    # Input type verification
    if not isinstance(type, str):
        raise TypeError('Expected \'type\' of type string.')
    elif column_formats and (not isinstance(column_formats, list) or 
                           len(column_formats) != 3):
        raise TypeError('Expected \'column_formats\' of type list of length 3.')
    elif not isinstance(upper_headers, bool):
        raise TypeError('Expected \'upper_headers\' of type bool.')
    elif column_formats and upper_headers:
        raise ValueError('Expect one kwarg, got two.')
    # Processing
    if type not in TableFormatter._formats:
        __import__(f'{__package__}.formats.{type}')
    formatter_cls = TableFormatter._formats.get(type)
    if not formatter_cls:
        raise RuntimeError('Unknown format %s' % type)
    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
            formats = column_formats
    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass
    return formatter_cls()
