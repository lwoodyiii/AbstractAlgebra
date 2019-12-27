class Set:

    def __init__(self, s):
        super().__init__()
        self.elements = s
    

    def pop(self):
        a = self.elements.pop()
        self.elements.add(a)
        return a

    def __contains__(self, item):
        return self.elements.__contains__(item)