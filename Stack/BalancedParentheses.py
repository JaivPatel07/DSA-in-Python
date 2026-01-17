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

    case1='()'
    case2='()[]{}'
    case3='(]'
    case4='([)]'

    pairs={  ')':'(',']':'[','}':'{'  }

    def verify(s):
        for char in s:
            if char in pairs:
                if stack.is_empty() or stack.pop()!=pairs[char]:
                    return False
            else:
                stack.push(char)
        return stack.is_empty()
    print(verify(case1)) # True
    print(verify(case2)) # True
    print(verify(case3)) # False
    print(verify(case4)) # False
            
                 
      


