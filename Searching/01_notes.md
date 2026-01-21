# Searching Algorithms – Complete Notes (MD)

---

## 📌 What is Searching?

**Searching** is the process of finding an element (key/target) in a data structure like an array, list, or string.

---

## 🔹 Types of Searching

1. **Linear Search**
2. **Binary Search**
3. **Jump Search**
4. **Interpolation Search**
5. **Exponential Search**

---

## 1️⃣ Linear Search

### 📖 Concept

* Check elements **one by one**
* Works on **sorted & unsorted** data

### ✅ Algorithm

1. Start from index 0
2. Compare each element with target
3. Stop if found or array ends

### 💻 Code (Python)

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

### ⏱ Time Complexity

| Case    | Complexity |
| ------- | ---------- |
| Best    | O(1)       |
| Average | O(n)       |
| Worst   | O(n)       |

### ✔ Pros / ❌ Cons

✔ Simple
❌ Slow for large data

---

## 2️⃣ Binary Search (Very Important ⭐⭐)

### 📖 Concept

* Works only on **sorted arrays**
* Divide array into halves

### ✅ Algorithm

1. Find mid element
2. Compare with target
3. Eliminate half
4. Repeat

### 💻 Code (Iterative)

```python
def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

### ⏱ Time Complexity

| Case    | Complexity |
| ------- | ---------- |
| Best    | O(1)       |
| Average | O(log n)   |
| Worst   | O(log n)   |

⚠️ **Array must be sorted**

---

## 3️⃣ Jump Search

### 📖 Concept

* Jump by fixed block size
* Then do linear search in block

### 💻 Code

```python
import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1
```

### ⏱ Time Complexity

`O(√n)`

---

## 4️⃣ Interpolation Search

### 📖 Concept

* Improved binary search
* Uses **position formula**
* Best for **uniformly distributed data**

### 💻 Code

```python
def interpolation_search(arr, target):
    low, high = 0, len(arr)-1

    while low <= high and target >= arr[low] and target <= arr[high]:
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1
```

### ⏱ Time Complexity

| Case    | Complexity   |
| ------- | ------------ |
| Best    | O(1)         |
| Average | O(log log n) |
| Worst   | O(n)         |

---

## 5️⃣ Exponential Search

### 📖 Concept

* Used for **infinite / unbounded arrays**
* Find range → apply binary search

### 💻 Code

```python
def exponential_search(arr, target):
    if arr[0] == target:
        return 0

    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2

    return binary_search(arr[i//2:min(i, len(arr))], target)
```

### ⏱ Time Complexity

`O(log n)`

---

## 🔍 Comparison Table

| Algorithm     | Sorted Needed | Time Complexity |
| ------------- | ------------- | --------------- |
| Linear        | ❌             | O(n)            |
| Binary        | ✅             | O(log n)        |
| Jump          | ✅             | O(√n)           |
| Interpolation | ✅             | O(log log n)    |
| Exponential   | ✅             | O(log n)        |

---

## 🎯 Real-Life Examples

* **Linear Search** → Find contact in phone list
* **Binary Search** → Dictionary word lookup
* **Jump Search** → Page navigation

---

## ⚠️ Common Mistakes

* Using binary search on unsorted array ❌
* Overflow while calculating mid ❌
* Infinite loop in while condition ❌

---

## 📌 Interview Tips

* Always ask: **Is data sorted?**
* Prefer **Binary Search** for large sorted data
* Know time complexity by heart

---
