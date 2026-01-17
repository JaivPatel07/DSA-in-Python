# 📚 Stack Data Structure – Complete Notes

## 1. What is a Stack?

A **stack** is a **linear data structure** that follows the principle:

> **LIFO – Last In, First Out**

The element inserted last is removed first, similar to a stack of plates.

---

## 2. Basic Terminology

* **Push**: Insert an element into the stack
* **Pop**: Remove the top element from the stack
* **Peek / Top**: View the top element without removing it
* **Overflow**: Trying to push when stack is full
* **Underflow**: Trying to pop when stack is empty

---

## 3. Stack Characteristics

* Access allowed from **only one end (top)**
* No random access
* Operations are fast: **O(1)**
* Can be implemented using **array** or **linked list**

---

## 4. Stack Operations

### 4.1 Push Operation

* Check overflow
* Increase top
* Insert element

### 4.2 Pop Operation

* Check underflow
* Remove top element
* Decrease top

### 4.3 Peek Operation

* Returns top element
* Does not modify stack

---

## 5. Stack Implementation

### 5.1 Stack Using Array

```python
class Stack:
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity

    def push(self, x):
        if len(self.stack) == self.capacity:
            print("Stack Overflow")
            return
        self.stack.append(x)

    def pop(self):
        if not self.stack:
            print("Stack Underflow")
            return
        return self.stack.pop()

    def peek(self):
        return self.stack[-1] if self.stack else None
```

---

### 5.2 Stack Using Linked List

* Push and pop from **head**
* No size limit

---

## 6. Time & Space Complexity

| Operation | Time Complexity |
| --------- | --------------- |
| Push      | O(1)            |
| Pop       | O(1)            |
| Peek      | O(1)            |

Space Complexity: **O(n)**

---

## 7. Applications of Stack

* Function calls (Call Stack)
* Expression evaluation
* Parenthesis checking
* Undo / Redo operations
* Backtracking
* Reversal of string or array

---

## 8. Expression Evaluation

### 8.1 Infix Expression

* Example: `A + B`

### 8.2 Prefix Expression

* Example: `+ A B`

### 8.3 Postfix Expression

* Example: `A B +`

👉 **Postfix & Prefix evaluation is easiest using stack**

---

## 9. Important Stack Problems

* Valid Parentheses
* Next Greater Element
* Stock Span Problem
* Largest Rectangle in Histogram
* Min Stack
* Reverse Stack using recursion

---

## 10. Stack vs Queue

| Stack             | Queue              |
| ----------------- | ------------------ |
| LIFO              | FIFO               |
| One end access    | Two end access     |
| Used in recursion | Used in scheduling |

---

## 11. Interview Tips 💡

* Always check overflow & underflow
* Use stack for **"previous" or "next" element** problems
* Think of stack when order needs to be reversed
* Use auxiliary stack when needed

---

## 12. Advantages & Disadvantages

### Advantages

* Simple implementation
* Fast operations
* Efficient memory usage

### Disadvantages

* Limited access
* Fixed size (array implementation)

---
