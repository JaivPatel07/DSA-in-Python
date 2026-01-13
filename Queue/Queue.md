# 📦 Queue Data Structure – Complete Notes

## 1. What is a Queue?

A **queue** is a **linear data structure** that follows the principle:

> **FIFO – First In, First Out**

The element inserted first is removed first, just like a real-life queue (line).

---

## 2. Basic Terminology

* **Enqueue**: Insert an element at the rear
* **Dequeue**: Remove an element from the front
* **Front**: First element of the queue
* **Rear**: Last element of the queue
* **Overflow**: Queue is full
* **Underflow**: Queue is empty

---

## 3. Queue Characteristics

* Insertion at **rear**, deletion from **front**
* No random access
* Operations are efficient: **O(1)**
* Can be implemented using **array** or **linked list**

---

## 4. Queue Operations

### 4.1 Enqueue Operation

* Check overflow
* Insert element at rear
* Move rear pointer

### 4.2 Dequeue Operation

* Check underflow
* Remove element from front
* Move front pointer

### 4.3 Peek Operation

* View front element without removing it

---

## 5. Queue Implementation

### 5.1 Queue Using Array

```python
class Queue:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity

    def enqueue(self, x):
        if len(self.queue) == self.capacity:
            print("Queue Overflow")
            return
        self.queue.append(x)

    def dequeue(self):
        if not self.queue:
            print("Queue Underflow")
            return
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0] if self.queue else None
```

---

### 5.2 Queue Using Linked List

* Enqueue at tail
* Dequeue from head
* No fixed size limit

---

## 6. Types of Queue

### 6.1 Simple Queue

* Standard FIFO behavior

### 6.2 Circular Queue

* Last position connects to first
* Efficient memory usage

### 6.3 Deque (Double Ended Queue)

* Insertion and deletion at both ends

### 6.4 Priority Queue

* Each element has priority
* Highest priority served first

---

## 7. Time & Space Complexity

| Operation | Time Complexity |
| --------- | --------------- |
| Enqueue   | O(1)            |
| Dequeue   | O(1)            |
| Peek      | O(1)            |

Space Complexity: **O(n)**

---

## 8. Applications of Queue

* CPU scheduling
* Printer scheduling
* Breadth First Search (BFS)
* Call center systems
* Task scheduling

---

## 9. Important Queue Problems

* Implement Queue using Stack
* Sliding Window Maximum
* First Non-Repeating Character
* Circular Queue design
* BFS traversal

---

## 10. Queue vs Stack

| Queue              | Stack             |
| ------------------ | ----------------- |
| FIFO               | LIFO              |
| Two-end operation  | One-end operation |
| Used in scheduling | Used in recursion |

---

## 11. Interview Tips 💡

* Clarify type of queue
* Circular queue avoids wasted space
* Use deque for sliding window problems
* BFS always uses queue

---

## 12. Advantages & Disadvantages

### Advantages

* Fair processing order
* Simple logic
* Efficient for scheduling

### Disadvantages

* Limited access
* Fixed size in array implementation

---

## 13. Summary

* Queue follows **FIFO**
* Enqueue & Dequeue are core operations
* Multiple variations exist
* Widely used in real-world systems

---

✨ *Queues keep systems organized and fair!*
