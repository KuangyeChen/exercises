class Stack:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.in_s1 = True

    def move_to_s1(self):
        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())

    def move_to_s2(self):
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())

    def enqueue(self, x):
        if not self.in_s1:
            self.move_to_s1()
        self.s1.append(x)

    def remove(self):
        if self.in_s1:
            self.move_to_s2()
        return self.s2.pop()
