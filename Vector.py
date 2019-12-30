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

    def __rmul__(self, other):
        return self.scalar_multiplication(other)
    
    def __mul__(self, other):
        return self.scalar_multiplication(other)

    def __eq__(self, value):
        return (self.elements == value.elements)

    def __add__(self, other):
        
