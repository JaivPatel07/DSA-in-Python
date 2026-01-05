"""
============================================================
QUEUE IN PYTHON
============================================================

This file contains:
1. What is Queue
2. FIFO principle
3. Queue operations
4. Types of Queue
5. Why Queue is useful
6. OOPS-based Queue implementation
7. Time complexity
8. Real-life applications

You can READ this file as NOTES and also RUN it.

============================================================
WHAT IS A QUEUE?
============================================================
A Queue is a LINEAR DATA STRUCTURE that follows:

    FIFO → First In, First Out

Example:
- Line at ticket counter
- Printer queue
- CPU scheduling

Two ends are used:
- Rear  → insertion (enqueue)
- Front → deletion (dequeue)

============================================================
QUEUE OPERATIONS
============================================================
1. enqueue → Insert element at rear
2. dequeue → Remove element from front
3. front   → Get first element
4. rear    → Get last element
5. isEmpty → Check if queue is empty
6. isFull  → Check if queue is full

============================================================
TYPES OF QUEUE
============================================================
1. Simple Queue
2. Circular Queue
3. Priority Queue
4. Deque (Double Ended Queue)

============================================================
WHY USE OOPS FOR QUEUE?
============================================================
✔ Code reusability
✔ Better structure
✔ Easy maintenance
✔ Used in real-world systems

============================================================
QUEUE IMPLEMENTATION USING OOPS
============================================================
"""

class Queue(object):
    """
    Queue class using OOPS
    Follows FIFO principle
    """

    def __init__(self, capacity):
        """
        Constructor
        capacity : maximum size of queue
        """
        self.capacity = capacity
        self.queue = []

    # -------------------------------------------------
    # ENQUEUE OPERATION
    # -------------------------------------------------
    def enqueue(self, item):
        """
        Insert element at rear
        """
        if self.isFull():
            print("Queue Overflow")
            return
        self.queue.append(item)
        print(f"Enqueued: {item}")

    # -------------------------------------------------
    # DEQUEUE OPERATION
    # -------------------------------------------------
    def dequeue(self):
        """
        Remove element from front
        """
        if self.isEmpty():
            print("Queue Underflow")
            return None
        return self.queue.pop(0)

    # -------------------------------------------------
    # FRONT ELEMENT
    # -------------------------------------------------
    def front(self):
        if self.isEmpty():
            return None
        return self.queue[0]

    # -------------------------------------------------
    # REAR ELEMENT
    # -------------------------------------------------
    def rear(self):
        if self.isEmpty():
            return None
        return self.queue[-1]

    # -------------------------------------------------
    # CHECK EMPTY
    # -------------------------------------------------
    def isEmpty(self):
        return len(self.queue) == 0

    # -------------------------------------------------
    # CHECK FULL
    # -------------------------------------------------
    def isFull(self):
        return len(self.queue) == self.capacity

    # -------------------------------------------------
    # DISPLAY QUEUE
    # -------------------------------------------------
    def display(self):
        print("Queue elements:", self.queue)


"""
============================================================
TIME COMPLEXITY
============================================================
enqueue → O(1)
dequeue → O(n)  (because of pop(0))
front   → O(1)

NOTE:
Using collections.deque gives O(1) dequeue

============================================================
REAL LIFE APPLICATIONS OF QUEUE
============================================================
1. CPU scheduling
2. Printer queue
3. Breadth First Search (BFS)
4. Customer service systems
5. Data buffering

============================================================
EXAM / INTERVIEW ONE-LINERS
============================================================
• Queue follows FIFO principle
• Insertion at rear, deletion at front
• Queue is used in scheduling problems
• BFS uses Queue data structure

============================================================
DRIVER CODE (RUN THIS)
============================================================
"""

if __name__ == "__main__":
    q = Queue(3)

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)   # Overflow

    q.display()

    print("Front element:", q.front())
    print("Dequeued:", q.dequeue())
    print("Dequeued:", q.dequeue())

    q.display()

"""
============================================================
FINAL SUMMARY
============================================================
Queue is a FIFO data structure widely used
in real-life scheduling and traversal problems.
============================================================
"""
