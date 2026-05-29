import sys

def _init():
    # Get callers local variables
    locs = sys._getframe(1).f_locals
    self = locs['self']
    for name, val in locs.items():
        if name == 'self': continue
        setattr(self, name, val)

class Stock:
    def __init__(self, name, shares, price):
        _init()
