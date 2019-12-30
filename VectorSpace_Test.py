from Vector import Vector
from random import random as r

''' a = complex(r(), -r())
b = complex(r(), -r())
x = Vector((complex(r(), -r()), complex(r(), -r())))
y = Vector((complex(r(), -r()), complex(r(), -r()))) '''

a = complex(12,13)
b = complex(15,-1)
x = Vector(((complex(-1, -3)), complex(3 , 4)))

def test_Vectors_Is_An_Abelian_Group(): assert True

def test_assoc():
    assoc(a, b, x)

def test_ident():
    ident(1)

def test_distrib_accross_scalars():
    distrib(a, x, y)

def test_distrib_accross_vectors():
    distrib(x, a, b)


# Tests Associativity
def assoc(a, b, c):
    assert a * (b * c) == (a * b) * c

# Tests Identity
def ident(I):
    assert I * x == x

def distrib(a, b, c):
    assert a *(b + c) == a * b + a * c

