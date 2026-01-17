# Easy one
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        x = self.stack.pop()
        if x == self.min_stack[-1]:
            self.min_stack.pop()

    def get_min(self):
        return self.min_stack[-1]

# more complex
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, x):
        if not self.stack:
            self.stack.append(x)
            self.min_val = x
        elif x >= self.min_val:
            self.stack.append(x)
        else:
            encoded = 2*x - self.min_val
            self.stack.append(encoded)
            self.min_val = x

    def pop(self):
        top = self.stack.pop()
        if top < self.min_val:
            self.min_val = 2*self.min_val - top

    def get_min(self):
        return self.min_val

