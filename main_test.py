#Testing an Abelian Group of in C
import cmath
import math as m

def test_closure():
    a = 1 + 1j
    b = 2 + 2j
    c = 3 + 3j
    c = a * b
    assert type(c) == type(a)

def test_associativity():
    a = 1 + 1j
    b = 2 + 2j
    c = 3 + 3j
    assert a * (b * c) == (a * b) * c

def test_identity():
    a = 1 + 1j
    assert a * 1 == a

def test_inverse():
    a = 1 + 1j
    assert a * (1/a)== 1