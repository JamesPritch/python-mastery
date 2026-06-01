import sys
import inspect

class Structure:
    def __repr__(self):
        return '%s(%s)' % (type(self).__name__,
                           ', '.join(repr(getattr(self, name)) for name in self._fields))
    def __setattr__(self, name, value):
        if name not in self._fields and name[0] != '_':
            raise AttributeError(f'No attribute {name}')
        super().__setattr__(name, value)

    @staticmethod
    def _init():
        # Get callers local variables
        locs = sys._getframe(1).f_locals
        self = locs['self']
        for name, val in locs.items():
            if name == 'self': continue
            setattr(self, name, val)
    @classmethod
    def set_fields(cls):
        sig = inspect.signature(cls)
        cls._fields = tuple(sig.parameters)

