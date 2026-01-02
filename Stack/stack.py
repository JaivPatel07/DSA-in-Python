"""
============================================================
STACK IN PYTHON - OOPS (BEGINNER FRIENDLY NOTES)
============================================================

This file contains:
1. What is Stack
2. LIFO principle
3. Stack operations
4. Why Stack is useful
5. OOPS-based Stack implementation
6. Time complexity
7. Real-life applications

You can READ this file as NOTES and also RUN it.

============================================================
WHAT IS A STACK?
============================================================
A Stack is a LINEAR DATA STRUCTURE that follows:

    LIFO → Last In, First Out

Example:
- Stack of plates
- Undo / Redo
- Browser back button

Only ONE END is used:
- Insertion (push)
- Deletion (pop)

============================================================
STACK OPERATIONS
============================================================
1. push  → Insert element into stack
2. pop   → Remove top element
3. peek  → View top element without removing
4. isEmpty → Check if stack is empty
5. isFull  → Check if stack is full

============================================================
WHY USE OOPS FOR STACK?
============================================================
✔ Code is reusable
✔ Data is secure (encapsulation)
✔ Easy to maintain and extend
✔ Used in real applications

============================================================
STACK IMPLEMENTATION USING OOPS
============================================================
"""

class Stack(object):
    """
    Stack class using OOPS
    Follows LIFO principle
    """

    def __init__(self, capacity):
        """
        Constructor
        capacity : maximum size of stack
        """
        self.capacity = capacity
        self.stack = []

    # -------------------------------------------------
    # PUSH OPERATION
    # -------------------------------------------------
    def push(self, item):
        """
        Insert element into stack
        """
        if self.isFull():
            print("Stack Overflow")
            return
        self.stack.append(item)
        print(f"Pushed: {item}")

    # -------------------------------------------------
    # POP OPERATION
    # -------------------------------------------------
    def pop(self):
        """
        Remove top element from stack
        """
        if self.isEmpty():
            print("Stack Underflow")
            return None
        return self.stack.pop()

    # -------------------------------------------------
    # PEEK OPERATION
    # -------------------------------------------------
    def peek(self):
        """
        Return top element without removing
        """
        if self.isEmpty():
            return None
        return self.stack[-1]

    # -------------------------------------------------
    # CHECK EMPTY
    # -------------------------------------------------
    def isEmpty(self):
        return len(self.stack) == 0

    # -------------------------------------------------
    # CHECK FULL
    # -------------------------------------------------
    def isFull(self):
        return len(self.stack) == self.capacity

    # -------------------------------------------------
    # DISPLAY STACK
    # -------------------------------------------------
    def display(self):
        print("Stack elements:", self.stack)


"""
============================================================
TIME COMPLEXITY
============================================================
push  → O(1)
pop   → O(1)
peek  → O(1)

============================================================
REAL LIFE APPLICATIONS OF STACK
============================================================
1. Function call stack
2. Undo / Redo operations
3. Expression evaluation
4. Parenthesis checking
5. Depth First Search (DFS)

============================================================
EXAM / INTERVIEW ONE-LINERS
============================================================
• Stack follows LIFO principle
• Insertion and deletion happen at one end
• Stack can be implemented using array or linked list
• push and pop operations take O(1) time

============================================================
DRIVER CODE (RUN THIS)
============================================================
"""

if __name__ == "__main__":
    s = Stack(3)

    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)   # Overflow

    s.display()

    print("Top element:", s.peek())
    print("Popped:", s.pop())
    print("Popped:", s.pop())

    s.display()

"""
============================================================
FINAL SUMMARY
============================================================
Stack is a simple and powerful data structure
that follows LIFO and is widely used in
real-world and interview problems.
============================================================
"""
