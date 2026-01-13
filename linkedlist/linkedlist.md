# 🔗 Linked List Data Structure – Complete Notes

## 1. What is a Linked List?

A **linked list** is a **linear data structure** where elements (nodes) are stored in **non-contiguous memory locations**. Each node contains **data** and a **reference (pointer)** to the next node.

Unlike arrays, linked lists do not require continuous memory and allow efficient insertion and deletion.

---

## 2. Basic Terminology

* **Node**: A unit containing data and pointer(s)
* **Head**: First node of the linked list
* **Tail**: Last node of the linked list
* **Pointer / Reference**: Stores address of next node
* **NULL**: Indicates end of list

---

## 3. Characteristics of Linked List

* Dynamic size
* No random access
* Efficient insertion & deletion
* Extra memory required for pointers

---

## 4. Types of Linked List

### 4.1 Singly Linked List

* Each node points to the **next node** only

```
[data | next] → [data | next] → NULL
```

---

### 4.2 Doubly Linked List

* Each node has two pointers:

  * **prev** → previous node
  * **next** → next node

```
NULL ← [prev | data | next] ↔ [prev | data | next] → NULL
```

---

### 4.3 Circular Linked List

* Last node points back to the **head**
* No NULL pointer

```
[data | next] → [data | next]
     ↑___________________|
```

---

## 5. Linked List Implementation

### 5.1 Singly Linked List (Python)

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

---

## 6. Common Linked List Operations

* Traversal
* Insertion

  * At beginning
  * At end
  * At given position
* Deletion

  * From beginning
  * From end
  * By value / position
* Searching
* Reversing

---

## 7. Time & Space Complexity

### Singly Linked List

| Operation     | Time Complexity |
| ------------- | --------------- |
| Access        | O(n)            |
| Search        | O(n)            |
| Insert (head) | O(1)            |
| Delete (head) | O(1)            |

Space Complexity: **O(n)**

---

## 8. Advantages & Disadvantages

### Advantages

* Dynamic memory allocation
* Efficient insertion & deletion
* No memory wastage

### Disadvantages

* Extra memory for pointers
* No random access
* Slower traversal than arrays

---

## 9. Important Linked List Problems

* Reverse Linked List
* Detect Cycle (Floyd’s Algorithm)
* Middle of Linked List
* Merge Two Sorted Lists
* Remove Nth Node from End
* Palindrome Linked List
* Rotate Linked List

---

## 10. Fast & Slow Pointer Technique 🐢🐇

* Uses two pointers moving at different speeds
* Commonly used to:

  * Detect cycles
  * Find middle node

---

## 11. Linked List vs Array

| Linked List             | Array                     |
| ----------------------- | ------------------------- |
| Dynamic size            | Fixed size                |
| No random access        | Random access             |
| Extra memory            | Memory efficient          |
| Easy insertion/deletion | Costly insertion/deletion |

---

## 12. Interview Tips 💡

* Always handle **edge cases** (empty list, one node)
* Use dummy node to simplify logic
* Draw list before coding
* Practice pointer manipulation carefully

---

## 13. Real-World Applications

* Music playlist
* Browser navigation (back/forward)
* Undo/Redo operations
* Memory management

---