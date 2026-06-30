import inspect
from functools import wraps
import decimal

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

    # Collect derived classes into a dict
    validators = {}
    @classmethod
    def __init_subclass__(cls):
        cls.validators[cls.__name__] = cls
    
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

_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('Complex', complex),
    ('Decimal', decimal.Decimal),
    ('List', list),
    ('Bool', bool),
    ('String', str)
]

globals().update((name, type(name, (Typed,), {'expected_type':ty}))
                 for name, ty in _typed_classes)

class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass

def isvalidator(item):
    return isinstance(item, type) and issubclass(item, Validator)

def validated(func):
    sig = inspect.signature(func)

    # Get the function annotations
    annotations = { name:val for name, val in func.__annotations__.items()
                    if isvalidator(val) }

    # Get the return annotation (if any)
    retcheck = annotations.pop('return', None)

    @wraps(func)

    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        errors = []

        # Enforce argument checks
        for name, validator in annotations.items():
            try:
                validator.check(bound.arguments[name])
            except Exception as e:
                errors.append(f'  {name}: {e}')

        if errors:
            raise TypeError('Bad Arguments\n' + '\n'.join(errors))

        result = func(*args, **kwargs)

        # Enforce return check (if any)
        if retcheck:
            try:
                retcheck.check(result)
            except Exception as e:
                raise TypeError(f'Bad return: {e}') from None
        return result
    return wrapper

def enforce(**annotations):
    retcheck = annotations.pop('return_', None)

    def decorate(func):
        sig = inspect.signature(func)

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound = sig.bind(*args, **kwargs)
            errors = []

            # Enforce argument checks
            for name, validator in annotations.items():
                try:
                    validator.check(bound.arguments[name])
                except Exception as e:
                    errors.append(f'    {name}: {e}')

            if errors:
                raise TypeError('Bad Arguments\n' + '\n'.join(errors))

            result = func(*args, **kwargs)

            if retcheck:
                try:
                    retcheck.check(result)
                except Exception as e:
                    raise TypeError(f'Bad return: {e}') from None
            return result
        return wrapper
    return decorate

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
    
    @validated
    def sell(self, nshares:PositiveInteger):
        self.shares -= nshares

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)
    
    @property
    def cost(self):
        return self.shares * self.price
