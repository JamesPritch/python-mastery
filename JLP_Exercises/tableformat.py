from abc import ABC, abstractmethod

# Classes
class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass
    @abstractmethod
    def row(self, rowdata):
        pass

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(('-'*10 + ' ')*len(headers))
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))
    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(str(h) for h in headers))
    def row(self, rowdata):
        print(','.join(str(d) for d in rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr> <th>' + '</th> <th>'.join(str(h) for h in headers) + '</th> </tr>')
    def row(self, rowdata):
        print('<tr> <td>' + '</td> <td>'.join(str(d) for d in rowdata) + '</td> </tr>')

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
