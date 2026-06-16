import sys
from validate0 import Validator, validated
from collections import ChainMap

class StructureMeta(type):
    @classmethod
    def __prepare__(meta, clsname, bases):
        return ChainMap({}, Validator.validators)
    
    @staticmethod
    def __new__(meta, name, bases, methods):
        methods = methods.maps[0]
        return super().__new__(meta, name, bases, methods)

class Structure(metaclass = StructureMeta):
    _types = ()

    def __repr__(self):
        return '%s(%s)' % (type(self).__name__,
                           ', '.join(repr(getattr(self, name)) for name in self._fields))
    def __setattr__(self, name, value):
        if name not in self._fields and name[0] != '_':
            raise AttributeError(f'No attribute {name}')
        super().__setattr__(name, value)

    @classmethod
    def create_init(cls):
        # Get callers local variables
        sys._getframe(1).f_locals
        argstr = ', '.join(cls._fields)
        code = f'def __init__(self, {argstr}):\n'
        for name in cls._fields:
            code += f'    self.{name} = {name}\n'
        locs = {}
        exec(code, locs)
        cls.__init__ = locs['__init__']
    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)
    @classmethod
    def from_row(cls, row):
        rowdata = [func(val) for func, val in zip(cls._types, row)]
        return cls(*rowdata)

def validate_attributes(cls):
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)
        elif callable(val) and val.__annotations__:
            setattr(cls, name, validated(val))
    
    cls._fields = tuple([val.name for val in validators])
    
    cls._types = tuple([getattr(val, 'expected_type') for val in validators])

    cls.create_init()
    return cls

def typed_structure(clsname, **validators):
    cls = type(clsname, (Structure,), validators)
    return cls
