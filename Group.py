from Set import Set

class Group(Set):
    def __init__(self, s):
        super().__init__(s)
        self.identity = 1

    def inv(self, x): pass
        
    