import csv
import sys
from decimal import Decimal

class Stock:

    _types = (str, int, float)
    __slots__ = ('name', '_shares', '_price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def __str__(self):
        return str(str(self.name), str(self.shares), str(self.price))
    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
    def __eq__(self, value):
        return isinstance(value, Stock) and ((self.name, self.shares, self.price) ==
                                             (value.name, value.shares, value.price))
    
    def sell(self, nshares):
        self.shares -= nshares

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)
    
    @property
    def cost(self):
        return self.shares * self.price
    @property
    def shares(self):
        return self._shares
    @property
    def price(self):
        return self._price
    
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        elif value < 0:
            raise ValueError('shares must be >= 0')
        self._shares = value
    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError('Expected float')
        elif value < 0:
            raise ValueError('price must be >= 0')
        self._price = value


class DStock(Stock):
    _types = (str, int, Decimal)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, Decimal):
            raise TypeError('Expected Decimal')
        elif value < 0:
            raise ValueError('price must be >= 0')
        self._price = value


class redirect_stdout:
    def __init__(self, out_file):
        self.out_file = out_file
    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self.out_file
        return self.out_file
    def __exit__(self, ty, val, tb):
        sys.stdout = self.stdout


def print_portfolio(data):
    print('%10s %10s %10s' % (headers[0].capitalize(), headers[1].capitalize(), headers[2].capitalize()))
    print('__________ __________ __________')
    for s in data:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))