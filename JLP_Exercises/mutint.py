from functools import total_ordering

@total_ordering
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            try:
                self.value = int(float(value))
                print('Don\'t be a silly Billy, your input has been rounded down.')
            except:
                print('Please refrain from being a clot. This is a function for integers. Your input has been set to zero.')
                self.value = 0
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return f'MutInt({self.value!r})'
    
    def __format__(self, fmt):
        return format(self.value, fmt)
    
    def __add__(self, other):
        if isinstance(other, MutInt):
            return MutInt(self.value+other.value)
        elif isinstance(other, int):
            return MutInt(self.value+other)
        else:
            return NotImplemented
        
    def __sub__(self, other):
        if isinstance(other, MutInt):
            return MutInt(self.value - other.value)
        elif isinstance(other, int):
            return MutInt(self.value-other)
        else:
            return NotImplemented
        
    def __iadd__(self, other):
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other 
            return self
        else:
            return NotImplemented
        
    def __isub__(self, other):
        if isinstance(other, MutInt):
            self.value -= other.value
            return self
        elif isinstance(other, int):
            self.value -= other
            return self
        else:
            return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, MutInt):
            return self.value == other.value 
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented
        
    def __lt__(self, other):
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    def __int__(self):
        return self.value
    
    def __float__(self):
        return float(self.value)

    __index__ = __int__

    __radd__ = __add__
    __rsub__ = __sub__