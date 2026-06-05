from validate0 import Integer, validated
from logcall import logformat, logged

@logged
def add(x: Integer, y: Integer) -> Integer:
    return x + y

@logged
def pow(x: Integer, y: Integer) -> Integer:
    return x ** y

@logformat('{func.__code__.co_filename}:{func.__name__}')
def mul(x: Integer, y: Integer) -> Integer:
    return x * y
