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


def infixToPostfix(s):
    stack = Stack()
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    result = ''

    for ch in s:
        if ch.isalnum():
            result += ch
        elif ch == '(':
            stack.push(ch)
        elif ch == ')':
            while not stack.is_empty() and stack.peek() != '(':
                result += stack.pop()
            stack.pop()
        else:
            while (not stack.is_empty() and
                   stack.peek() != '(' and
                   precedence[stack.peek()] >= precedence[ch]):
                result += stack.pop()
            stack.push(ch)
    while not stack.is_empty():
        result += stack.pop()

    return result


s = "A+(B*C)"
print(infixToPostfix(s))
