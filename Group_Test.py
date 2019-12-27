# Testing an Abelian Group of in C

from Group import Group
import random

# Global variables
g = Group()
a = random.sample(g.elements, 1)[0]
b = random.sample(g.elements, 1)[0]
c = random.sample(g.elements, 1)[0]

@classmethod
def setup_class(): pass

def test_closure():
    assert a * b in g

def test_associativity():
    assert a * (b * c) == (a * b) * c

def test_identity():
    assert a * g.identity == a

def test_inverse():
    def myInv(x):
        return 1/x
    g.inv = myInv
    assert a * g.inv(a) == g.identity

#Only an Abelian Group must be commutative
def test_commutativity():
    assert a + b == b + a


