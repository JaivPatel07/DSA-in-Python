# ============================================================
# BUBBLE SORT – BEGINNER FRIENDLY NOTES
# ============================================================

# WHAT IS BUBBLE SORT?
# Repeatedly compare adjacent elements and swap them if they are in wrong order.
# Largest element "bubbles" to the end in each pass.

# WHY NAME "BUBBLE"?
# Big elements move to the end like bubbles in water.

# ------------------------------------------------------------
# WHEN TO USE?
# - For learning sorting basics
# - NOT used in real problems (slow)

# ------------------------------------------------------------
# TIME & SPACE COMPLEXITY
# ------------------------------------------------------------
# Best Case   : O(n)    (already sorted, with optimization)
# Worst Case  : O(n^2)
# Average     : O(n^2)
# Space       : O(1)

# ------------------------------------------------------------
# BASIC BUBBLE SORT CODE
# ------------------------------------------------------------

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):                 # number of passes
        for j in range(0, n-i-1):      # compare adjacent elements
            if arr[j] > arr[j+1]:
                # swap
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [5, 3, 8, 4, 2]
bubble_sort(arr)
print(arr)   # [2, 3, 4, 5, 8]


# ------------------------------------------------------------
# OPTIMIZED BUBBLE SORT (IMPORTANT)
# ------------------------------------------------------------

# IDEA:
# If no swap happens in a pass → array is already sorted

def bubble_sort_optimized(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:     # no swap → stop early
            break

arr = [1, 2, 3, 4]
bubble_sort_optimized(arr)
print(arr)   # [1, 2, 3, 4]


# ------------------------------------------------------------
# STEP BY STEP WORKING (SMALL EXAMPLE)
# ------------------------------------------------------------

# arr = [4, 3, 1]

# Pass 1:
# (4,3) → swap → [3,4,1]
# (4,1) → swap → [3,1,4]

# Pass 2:
# (3,1) → swap → [1,3,4]

# Sorted


# ------------------------------------------------------------
# IMPORTANT INTERVIEW POINTS
# ------------------------------------------------------------

# - Stable sort (keeps order of equal elements)
# - In-place sorting (no extra memory)
# - Very slow for large input
# - Used only for teaching concepts


# ------------------------------------------------------------
# WHEN NOT TO USE BUBBLE SORT?
# ------------------------------------------------------------

# - Large arrays
# - Time-critical applications
# - Competitive programming


# ------------------------------------------------------------
# QUICK SUMMARY
# ------------------------------------------------------------

"""
Bubble Sort:
- Compare adjacent elements
- Swap if needed
- Largest element moves to end
- Time: O(n^2)
- Space: O(1)
- Use only for learning
"""
