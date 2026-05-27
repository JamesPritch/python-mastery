def typed_property(name, expected_type):
    private_name = '_' + name

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, val)

    return value

class String():
    def __init__(self, name = None):
        self.name = name
    def __get__(self, instance, owner):
        name = instance.__dict__[self.name]
        return lambda name:typed_property(name, str)
    def __set_name__(self, cls, name):
        self.name =  name

class Integer():
    def __init__(self, name = None):
        self.name = name
    def __get__(self, instance, owner):
        name = instance.__dict__[self.name]
        return lambda name:typed_property(name, int)
    def __set_name__(self, cls, name):
        self.name =  name

class Float():
    def __init__(self, name = None):
        self.name = name
    def __get__(self, instance, owner):
        name = instance.__dict__[self.name]
        return lambda name:typed_property(name, float)
    def __set_name__(self, cls, name):
        self.name =  name

class Stock:
    name = String()
    shares = Integer()
    price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
