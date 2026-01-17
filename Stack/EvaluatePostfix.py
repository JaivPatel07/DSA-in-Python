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

s='231*+9-'
def evaluatePostfix(s):
    stack =Stack()
    for i in s:
        if i=='+':
            stack.push(stack.pop()+stack.pop())
        elif i=='-':
            stack.push((-stack.pop())+(stack.pop()))
        elif i=='*':
            stack.push(stack.pop()*stack.pop())
        elif i=='/':
            stack.push((stack.pop()**-1)*(stack.pop()))
        else:
            stack.push(int(i))
    print(stack.pop())

evaluatePostfix(s) #-4
    

