from abc import ABC, abstractmethod
__all__ = ['create_formatter', 'print_table']

# Classes
class TableFormatter(ABC):
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

from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter
from .formats.text import TextTableFormatter

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
    elif type == 'html':
        if column_formats:
            class PortfolioFormatter(ColumnFormatMixin, HTMLTableFormatter):
                formats = column_formats
            return PortfolioFormatter()
        elif upper_headers:
            class PortfolioFormatter(UpperHeadersMixin, HTMLTableFormatter):
                pass
            return PortfolioFormatter()
        else:
            return HTMLTableFormatter()
    elif type == 'csv':
        if column_formats:
            class PortfolioFormatter(ColumnFormatMixin, CSVTableFormatter):
                formats = column_formats
            return PortfolioFormatter()
        elif upper_headers:
            class PortfolioFormatter(UpperHeadersMixin, CSVTableFormatter):
                pass
            return PortfolioFormatter()
        else:
            return CSVTableFormatter()
    elif type == 'text':
        if column_formats:
            class PortfolioFormatter(ColumnFormatMixin, TextTableFormatter):
                formats = column_formats
            return PortfolioFormatter()
        elif upper_headers:
            class PortfolioFormatter(UpperHeadersMixin, TextTableFormatter):
                pass
            return PortfolioFormatter()
        else:
            return TextTableFormatter()
    else:
        raise ValueError('Expected \'csv\', \'html\', or \'text\'.')
