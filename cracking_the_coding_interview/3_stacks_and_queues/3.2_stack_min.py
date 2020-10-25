class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        v, v_min = self.data[-1]
        self.data.append((x, min(v_min, x)))

    def pop(self):
        v, _ = self.data.pop()
        return v

    def min(self):
        return self.data[-1][1]
