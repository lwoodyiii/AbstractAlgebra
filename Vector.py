class Vector:
    def __init__(self, Tuple):
        super().__init__()
        self.elements = Tuple
        self.dim = len(Tuple)

    

    def multiply(self, other):
        x = []
        for i in self.elements:
            x.append(i * other)
        return Vector(tuple(x))
        
    def __rmul__(self, other):
        return self.multiply(other)
    
    def __mul__(self, other):
        return self.multiply(other)
