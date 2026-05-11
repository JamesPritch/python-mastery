from abc import ABC, abstractmethod

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


def print_table(data, fields, formatter):
    if not isinstance(data, TableFormatter):
        raise TypeError('Expected a TableFormatter')
    formatter.headings(fields)
    for s in data:
        rowdata = [getattr(s, fieldname) for fieldname in fields]
        formatter.row(rowdata)

def create_formatter(type):
    if not isinstance(type, str):
        raise TypeError('Expected string.')
    elif type == 'html':
        return HTMLTableFormatter()
    elif type == 'csv':
        return CSVTableFormatter()
    elif type == 'text':
        return TextTableFormatter()
    else:
        raise ValueError('Expected \'csv\', \'html\', or \'text\'.')