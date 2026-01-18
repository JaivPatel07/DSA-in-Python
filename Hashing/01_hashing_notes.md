# 🔑 Hashing Data Structure – Complete Notes

## 1. What is Hashing?

**Hashing** is a technique used to **map data to a fixed-size value** (hash code) using a **hash function**, enabling **fast insertion, deletion, and search**.

The data is stored in a **Hash Table**, where each key is converted into an index.

---

## 2. Hash Table

A **hash table** is a data structure that stores **key–value pairs** using a hash function to compute an index.

```text
Index = HashFunction(Key)
```

---

## 3. Hash Function

A **hash function**:

* Takes a key as input
* Produces an integer (hash value)
* Maps keys uniformly

### Properties of a Good Hash Function

* Deterministic
* Fast computation
* Uniform distribution
* Minimizes collisions

---

## 4. Collision

A **collision** occurs when **two keys map to the same index**.

### Causes

* Poor hash function
* Limited table size

---

## 5. Collision Resolution Techniques

### 5.1 Separate Chaining

* Each index stores a **linked list**
* Colliding elements are chained

```
Index → Node → Node → NULL
```

**Pros**:

* Simple
* No overflow

**Cons**:

* Extra memory

---

### 5.2 Open Addressing

All elements are stored in the table itself.

#### a) Linear Probing

```text
h(key) = (hash + i) % size
```

* Easy
* Causes clustering

#### b) Quadratic Probing

```text
h(key) = (hash + i²) % size
```

* Reduces clustering

#### c) Double Hashing

```text
h(key) = (hash1 + i × hash2) % size
```

* Best distribution

---

## 6. Load Factor (α)

```text
Load Factor = Number of Elements / Table Size
```

* Controls performance
* High load factor → more collisions

---

## 7. Hashing Operations

| Operation | Average Time | Worst Time |
| --------- | ------------ | ---------- |
| Insert    | O(1)         | O(n)       |
| Search    | O(1)         | O(n)       |
| Delete    | O(1)         | O(n)       |

---

## 8. Hash Map & Hash Set

### Hash Map

* Stores **key → value** pairs
* Example: Python `dict`

### Hash Set

* Stores **unique keys only**
* Example: Python `set`

---

## 9. Hashing in Python

```python
# Hash Map
mp = {"a": 1, "b": 2}

# Insert
mp["c"] = 3

# Search
print(mp.get("a"))

# Hash Set
st = set()
st.add(10)
```

---

## 10. Applications of Hashing

* Database indexing
* Caching
* Password storage
* Symbol tables
* Duplicate detection
* Frequency counting

---

## 11. Important Hashing Problems

* Two Sum
* Subarray Sum Equals K
* Longest Consecutive Sequence
* Group Anagrams
* First Non-Repeating Character
* Isomorphic Strings

---

## 12. Advantages & Disadvantages

### Advantages

* Very fast access
* Efficient for large data
* Simple API

### Disadvantages

* Collisions possible
* Extra memory
* No ordering

---

## 13. Hashing vs Sorting

| Hashing      | Sorting           |
| ------------ | ----------------- |
| O(1) lookup  | O(log n) lookup   |
| Unordered    | Ordered           |
| Extra memory | In-place possible |

---

## 14. Interview Tips 💡

* Think hashing for **frequency counting**
* Use hash set to detect duplicates
* Be careful with collisions
* Know time complexity clearly
