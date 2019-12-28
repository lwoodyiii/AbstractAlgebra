from Vector import Vector

def test_multiply():
    t = (1, 2, 3)
    v = Vector(t)
    test1 = v * 3
    test2 = 3 * v
    ansT = (3, 6, 9)
    ans = Vector(ansT)
    assert(test1 == ans)
    print(test1.elements)
    print(test2.elements)
    print(v.elements)
