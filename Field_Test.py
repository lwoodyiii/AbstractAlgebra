# Testing a Field

from Field import Field
import random

# Global variables
f = Field()
a = random.sample(f.elements, 1)[0]
b = random.sample(f.elements, 1)[0]
c = random.sample(f.elements, 1)[0]

def test_distributivity():
    assert a * (b + c) == a * b + a * c

# Should also test the field to see 
#    - if it's an Abelian Group for + with Identity element 0.
#    - if it's an Abelian Group for * without the number 0.
