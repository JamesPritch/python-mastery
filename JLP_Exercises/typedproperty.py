def typedproperty(expected_type):
    private_name = ''

    def __set_name__(self, cls, name):
        nonlocal private_name
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

String = lambda :typedproperty(str)
Integer = lambda :typedproperty(int)
Float = lambda :typedproperty(float)

class Stock:
    name = String()
    shares = Integer()
    price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
