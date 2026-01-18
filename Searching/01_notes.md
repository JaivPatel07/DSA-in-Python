# 🔁 Recursion & Backtracking – Complete Notes

## 1. What is Recursion?

**Recursion** is a programming technique where a function **calls itself** to solve a problem by breaking it into **smaller subproblems**.

A recursive solution works until it reaches a **base case**.

---

## 2. Components of Recursion

Every recursive function must have:

1. **Base Case** – stops recursion
2. **Recursive Case** – function calls itself

```python
def factorial(n):
    if n == 0:        # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case
```

---

## 3. How Recursion Works (Call Stack)

* Each recursive call is stored in the **call stack**
* Functions execute in **LIFO order**
* Deep recursion may cause **stack overflow**

---

## 4. Types of Recursion

### 4.1 Direct Recursion

Function calls itself directly.

### 4.2 Indirect Recursion

Function calls another function which calls the first one.

### 4.3 Tail Recursion

Recursive call is the **last statement** in function.

### 4.4 Head Recursion

Recursive call happens **before** processing.

---

## 5. Advantages & Disadvantages of Recursion

### Advantages

* Clean and readable code
* Easy to solve complex problems
* Matches mathematical definitions

### Disadvantages

* Extra memory (call stack)
* Slower than iteration
* Risk of stack overflow

---

## 6. What is Backtracking?

**Backtracking** is an algorithmic technique where we:

> Try a choice → If it fails, undo it → Try next choice

It is mainly used to **explore all possible solutions**.

Backtracking is usually implemented using **recursion**.

---

## 7. General Backtracking Template

```python
def backtrack(path, choices):
    if base_condition:
        result.append(path)
        return

    for choice in choices:
        path.append(choice)     # choose
        backtrack(path, choices)  # explore
        path.pop()              # un-choose
```

---

## 8. Types of Backtracking Problems

### 8.1 Decision Problems

* Check if solution exists

### 8.2 Optimization Problems

* Find best solution

### 8.3 Enumeration Problems

* Find all solutions

---

## 9. Recursion vs Backtracking

| Recursion                | Backtracking         |
| ------------------------ | -------------------- |
| Technique                | Algorithmic strategy |
| Breaks problem           | Explores choices     |
| May or may not backtrack | Always backtracks    |

---

## 10. Time & Space Complexity

* **Recursion**: Depends on depth of calls
* **Backtracking**: Often **exponential** (O(2ⁿ), O(n!))
* Space: O(depth of recursion)

---

## 11. Important Recursion Problems

* Factorial
* Fibonacci
* Power of a number
* Reverse a string
* Print subsequences
* Tower of Hanoi

---

## 12. Important Backtracking Problems

* Subsets
* Permutations
* Combinations
* N-Queens
* Sudoku Solver
* Rat in a Maze
* Word Search

---

## 13. Common Mistakes ⚠️

* Missing base case
* Incorrect backtracking (not undoing choice)
* Modifying global state incorrectly
* Infinite recursion

---

## 14. Interview Tips 💡

* Always define base case first
* Think in terms of **choices → recursion → backtrack**
* Use recursion tree visualization
* Practice small examples

