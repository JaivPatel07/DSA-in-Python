class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

if __name__ == "__main__":

    stack = Stack()
    s='123456789'
    for i in s:
        stack.push(i)
    
    new_s = ''
    while not stack.is_empty():
        new_s += stack.pop()
    print(new_s) # 987654321
        

    