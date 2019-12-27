class Set:
    def __init__(self):
        s = set()
        for i in range(1000):
            s.add(i+1)
        self.elements = s
        self.infinite_set = True

    def pop(self):
        a = self.elements.pop()
        self.elements.add(a)
        return a

    def __contains__(self, item):
        if self.infinite_set:
            self.elements.add(item)
            return True
        else:
            return self.elements.__contains__(item)
