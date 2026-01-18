class stack:
    def __init__(self , capacity):
        self.capacity = capacity
        self.stack = []

    def push(self , value):
        if self.capacity==len(self.stack):
            print("Stack Overflow")
            return
        self.stack.append(value)
        print(f"Pushed: {value}")
    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
            return None
        return self.stack.pop()
    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack)==0
    def isFull(self):
        return len(self.stack)==self.capacity
    def display(self):
        print("Stack elements:" , self.stack)

if __name__ == "__main__":
    s = stack(3)

    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)   # Overflow

    s.display()

    print("Top element:", s.peek())
    print("Popped:", s.pop())
    print("Popped:", s.pop())

    s.display()


