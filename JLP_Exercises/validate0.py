class Validator:
    def __init__(self, name=None):
        self.name = name
    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)
    def __set_name__(self, cls, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value
    
class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return super().check(value)
    
class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        return super().check(value)

class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if not len(value):
            raise ValueError('Must be non-empty')
        return super().check(value)

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str

class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass

class Stock:
    name   = NonEmptyString()
    shares = PositiveInteger()
    price  = PositiveFloat()

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
