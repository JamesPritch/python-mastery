from ..formatter import TableFormatter
from colorama import Fore

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(('-'*10 + ' ')*len(headers))
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))
    def row(self, rowdata):
        # Added colours for ticker pipeline
        if rowdata[2] > 0:
            print(Fore.GREEN + ' '.join('%10s' % d for d in rowdata))
        elif rowdata[2] < 0:
            print(Fore.RED + ' '.join('%10s' % d for d in rowdata))
        else:
            print(Fore.WHITE + ' '.join('%10s' % d for d in rowdata))
        print(Fore.WHITE + '', end = '')
        # Previous code
        # print(' '.join('%10s' % d for d in rowdata))
