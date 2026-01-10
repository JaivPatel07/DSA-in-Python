class queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
            return
        self.rear = (self.rear + 1) % self.capacity
        if len(self.queue) < self.capacity:
            self.queue.append(item)
        else:
            self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        index = self.front
        for _ in range(self.size):
            print(self.queue[index], end=" ")
            index = (index + 1) % self.capacity
        print()

    def reverse(self):
        stack = []
        while not self.is_empty():
            stack.append(self.dequeue())
        while stack:
            self.enqueue(stack.pop())
if __name__ == "__main__":
    q = queue(5)

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Original Queue:")
    q.display()

    q.reverse()

    print("Reversed Queue:")
    q.display()
