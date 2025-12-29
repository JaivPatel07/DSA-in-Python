# ============================================================
# SEARCHING – BEGINNER FRIENDLY NOTES
# ============================================================

# SEARCHING:
# Finding an element in a collection (array / list)

# ------------------------------------------------------------
# TYPES OF SEARCHING
# ------------------------------------------------------------

# 1. Linear Search
# 2. Binary Search

# ============================================================
# 1. LINEAR SEARCH
# ============================================================

# WHAT:
# Check each element one by one

# WHEN TO USE:
# - Array is unsorted
# - Small input size

# TIME:
# Best: O(1)
# Worst: O(n)

# SPACE:
# O(1)

# ------------------------------------------------------------
# LINEAR SEARCH CODE
# ------------------------------------------------------------

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [5, 3, 8, 2, 9]
print(linear_search(arr, 8))   # 2
print(linear_search(arr, 1))   # -1


# ============================================================
# 2. BINARY SEARCH
# ============================================================

# IMPORTANT:
# Array MUST be sorted

# WHAT:
# Repeatedly divide search space into half

# WHEN TO USE:
# - Sorted array
# - Large input size

# TIME:
# O(log n)

# SPACE:
# O(1) (iterative)

# ------------------------------------------------------------
# BINARY SEARCH (ITERATIVE)
# ------------------------------------------------------------

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = [2, 4, 6, 8, 10]
print(binary_search(arr, 6))   # 2
print(binary_search(arr, 7))   # -1


# ============================================================
# BINARY SEARCH RULES (IMPORTANT)
# ============================================================

# - Always use while left <= right
# - mid = (left + right) // 2
# - If target > mid → move left
# - If target < mid → move right

# COMMON MISTAKES:
# - Using binary search on unsorted array
# - Infinite loop (wrong mid update)


# ============================================================
# LINEAR vs BINARY (INTERVIEW)
# ============================================================

"""
LINEAR SEARCH:
- Works on unsorted data
- Simple
- Slow for large input

BINARY SEARCH:
- Needs sorted data
- Very fast
- Used in large datasets
"""


# ============================================================
# WHEN TO USE WHAT?
# ============================================================

"""
Unsorted array → Linear Search
Sorted array   → Binary Search
Small input    → Linear Search
Large input    → Binary Search
"""
