from ..formatter import TableFormatter

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr> <th>' + '</th> <th>'.join(str(h) for h in headers) + '</th> </tr>')
    def row(self, rowdata):
        print('<tr> <td>' + '</td> <td>'.join(str(d) for d in rowdata) + '</td> </tr>')
