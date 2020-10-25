class Stack:
    def __init__(self, size):
        self.data = [[]]
        self.size = size

    def push(self, x):
        if len(self.data[-1]) == self.size:
            self.data.append([])

        self.data[-1].append(x)

    def pop(self):
        v = self.data[-1].pop()
        if len(self.data[-1]) == 0:
            self.data.pop()
        return v

    def popAt(self, index):
        v = self.data[index].pop()
        if len(self.data[-1]) == 0:
            self.data.pop()
        return v
