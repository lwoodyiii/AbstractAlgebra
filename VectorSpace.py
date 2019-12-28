from Field import Field
from Group import Group

class VectorSpace:
    def __init__(self, f):
        super().__init__()
        self.field = f
        self.vectors = Group()
        self.vectors.identity = 0
