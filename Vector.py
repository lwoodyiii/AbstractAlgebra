class Vector:
    def __init__(self, t):
        super().__init__()
        self.elements = t
        self.dim = len(t)

    def scalar_multiplication(self, other):
        x = []
        for i in self.elements:
            x.append(i * other)
        return Vector(tuple(x))

    # Also known as the dot product
    def vector_inner_product(self, other):
        raise NotImplementedError

    def __rmul__(self, other):
        return self.scalar_multiplication(other)
   
    def __mul__(self, other):
        return self.scalar_multiplication(other)

    def __eq__(self, value):
        return (self.elements == value.elements)

    def __add__(self, other):
        x = []
        for i, j in zip(self.elements, other.elements):
            x.append(i + j)
        return Vector(tuple(x))

    def __radd__(self, other):
        x = []
        for i in self.elements:
            x.append(i + other)
        return Vector(tuple(x))
