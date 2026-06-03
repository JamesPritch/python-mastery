import validate0

# Refresh validator class
from validate0 import Integer

Integer.check(1)
Integer.check('one')

def add(x,y):
    Integer.check(x)
    Integer.check(y)
    return x+y

add(1,2)
add(1,'two')

# Create callable object
def add(x,y):
    return x + y

add = validate0.ValidatedFunction(add)
add(1,2)

# Enforcement
def add(x: Integer, y:Integer):
    return x + y

add = validate0.ValidatedFunction(add)
add(2,3)
add(1,'two')
