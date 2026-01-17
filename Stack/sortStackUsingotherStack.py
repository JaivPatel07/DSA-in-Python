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
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")
    def __str__(self):
        return str(self.items)
    
def sort_stack(stack1):
    temp1 = Stack()
    while not stack1.is_empty():
        x = stack1.pop()
        while not temp1.is_empty() and temp1.peek() > x:
            stack1.push(temp1.pop())
        temp1.push(x)
    return temp1


# Test
stack1 = Stack()
stack1.push(6)
stack1.push(2)
stack1.push(9)
stack1.push(30)
stack1.push(1)

sorted_stack = sort_stack(stack1)
print(sorted_stack)
