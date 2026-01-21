# Sorting Algorithms – Complete Notes (DSA)

---

## 📌 What is Sorting?

**Sorting** is the process of arranging data in a **particular order** (ascending or descending).

Example:

```
Unsorted: [5, 2, 9, 1]
Sorted:   [1, 2, 5, 9]
```

---

## 🔹 Types of Sorting Algorithms

* Bubble Sort
* Selection Sort
* Insertion Sort
* Merge Sort
* Quick Sort
* Heap Sort
* Counting Sort

---

## 1️⃣ Bubble Sort

### 📖 Concept

* Repeatedly swap **adjacent elements** if they are in wrong order
* Largest element moves to end in each pass

### 💻 Code (Python)

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```

### ⏱ Time Complexity

| Case    | Complexity |
| ------- | ---------- |
| Best    | O(n)       |
| Average | O(n²)      |
| Worst   | O(n²)      |

✔ Simple ❌ Slow

---

## 2️⃣ Selection Sort

### 📖 Concept

* Select minimum element and place at correct position

### 💻 Code

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
```

### ⏱ Time Complexity

`O(n²)` (all cases)

✔ No extra memory ❌ Many comparisons

---

## 3️⃣ Insertion Sort

### 📖 Concept

* Build sorted array one element at a time
* Like sorting playing cards

### 💻 Code

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
```

### ⏱ Time Complexity

| Case  | Complexity |
| ----- | ---------- |
| Best  | O(n)       |
| Worst | O(n²)      |

✔ Good for small data

---

## 4️⃣ Merge Sort (Very Important ⭐⭐)

### 📖 Concept

* Divide & Conquer algorithm
* Divide array → sort → merge

### 💻 Code

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
```

### ⏱ Time Complexity

`O(n log n)` (all cases)

✔ Stable ❌ Extra space

---

## 5️⃣ Quick Sort (Very Important ⭐⭐)

### 📖 Concept

* Choose pivot
* Partition array
* Recursively sort

### 💻 Code

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return left + mid + right
```

### ⏱ Time Complexity

| Case    | Complexity |
| ------- | ---------- |
| Best    | O(n log n) |
| Average | O(n log n) |
| Worst   | O(n²)      |

✔ Fast in practice ❌ Worst case

---

## 6️⃣ Heap Sort

### 📖 Concept

* Uses **Binary Heap**
* Max heap → repeatedly remove max

### ⏱ Time Complexity

`O(n log n)`

❌ Not stable

---

## 7️⃣ Counting Sort

### 📖 Concept

* Count frequency of elements
* Works for **small integer range**

### ⏱ Time Complexity

`O(n + k)`

✔ Very fast ❌ Limited range

---

## 📊 Comparison Table

| Algorithm | Time       | Space    | Stable |
| --------- | ---------- | -------- | ------ |
| Bubble    | O(n²)      | O(1)     | ✅      |
| Selection | O(n²)      | O(1)     | ❌      |
| Insertion | O(n²)      | O(1)     | ✅      |
| Merge     | O(n log n) | O(n)     | ✅      |
| Quick     | O(n log n) | O(log n) | ❌      |
| Heap      | O(n log n) | O(1)     | ❌      |

---

## ⚠️ Common Mistakes

* Using bubble sort for large data ❌
* Forgetting base case in recursion ❌
* Wrong pivot selection ❌

---

## 🎯 Interview Tips

* Always mention **time + space complexity**
* Know **stable vs unstable**
* Merge & Quick sort are most asked

---
