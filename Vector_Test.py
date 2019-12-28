from Vector import Vector

v1 = Vector(1, 2, 3)
v2 = Vector(2, 4, 5)

def test_scalar_multiplication():
    test1 = v1 * 3
    test2 = 3 * v1
    ans = Vector(3, 6, 9)
    assert(test1 == ans)
    assert(test2 == ans)
    assert(test1 == test2)

def test_vector_addition():
    test1 = v1 + v2
    test2 = v2 + v1
    ans = Vector(3,6,8)
    assert(test == ans)
    assert(test2 == ans)
    assert(test1 == test2)

def test_vector_multiplication():
    test1 = v1 * v2
    test2 = v2 * v1
