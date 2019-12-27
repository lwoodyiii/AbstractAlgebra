#Testing an Abelian Group of in C
from Group import Group

def init():
    s = set()
    for i in range(10000):
        s.add(i+1)
    g = Group(s)
    return g

def test_closure():
    g = init()
    a = g.pop()
    b = g.pop()
    assert a * b in g

def test_associativity():
    g = init()
    a = g.pop()
    print(a)
    b = g.pop()
    print(b)
    c = g.pop()
    assert a * (b * c) == (a * b) * c

def test_identity():
    g = init()
    a = g.pop()
    assert a * g.identity == a

def test_inverse():
    g = init()
    a = g.pop()
    def myInv(x):
        return 1/x
    g.inv = myInv
    assert a * g.inv(a) == g.identity

#Only an Abelian Group must be commutative
def test_commutativity():
    g = init()
    a = g.pop()
    b = g.pop()
    assert a + b == b + a

# Test for a Field
def test_distributivity():
    g = init()
    a = g.pop()
    b = g.pop()
    c = g.pop()
    assert a * (b + c) == a*b + a*c