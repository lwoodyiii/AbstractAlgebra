
from Group import Group

def test_main():
    g = Group()
    a = g.Op(1,1)
    assert a == 1