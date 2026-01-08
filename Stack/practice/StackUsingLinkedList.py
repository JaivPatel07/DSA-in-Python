class LinkedListStack:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self,capacity):
        self.head = None
        self.capacity = capacity
        self.size = 0
    
    def push(self, value):
        node = self.Node(value)
        if self.size < self.capacity:
            if self.head is None:
                self.head = node
            else:
                temp = self.head
                while temp.next is not None:
                    temp = temp.next
                temp.next = node
            self.size += 1
        else:
            print("Stack Overflow")
    def pop(self):
        if self.head is None:
            print("Stack Underflow")
            return None
        else:
            temp = self.head
            self.head = temp.next
            self.size -= 1
            return temp.data
    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.data
    def isEmpty(self):
        return self.head is None
    def isFull(self):
        return self.size == self.capacity
    def display(self):
        if self.head is None:
            print("Stack is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()

if __name__ == "__main__":
    s = LinkedListStack(3)

    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)   # Overflow

    s.display()

    print("Top element:", s.peek())
    print("Popped:", s.pop())
    print("Popped:", s.pop())

    s.display()

