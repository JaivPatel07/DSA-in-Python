# ============================================================
# QUICK SORT – BEGINNER FRIENDLY NOTES
# ============================================================

# WHAT IS QUICK SORT?
# Quick Sort is a Divide and Conquer algorithm.
# It selects a pivot element and places it at its correct position.
# Elements smaller go left, larger go right.

# ------------------------------------------------------------
# REAL LIFE EXAMPLE
# ------------------------------------------------------------
# Imagine choosing one student as a reference (pivot).
# Students shorter go to the left, taller to the right.
# Repeat this for each group.
# That’s Quick Sort.

# ------------------------------------------------------------
# WHEN TO USE?
# ------------------------------------------------------------
# - Very large datasets
# - Competitive programming
# - When memory usage should be low

# ------------------------------------------------------------
# TIME & SPACE COMPLEXITY
# ------------------------------------------------------------
# Best Case   : O(n log n)
# Average     : O(n log n)
# Worst Case  : O(n^2)   (bad pivot choice)
# Space       : O(log n)

# ------------------------------------------------------------
# QUICK SORT CODE
# ------------------------------------------------------------

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

arr = [5, 3, 8, 4, 2]
arr = quick_sort(arr)
print(arr)   # [2, 3, 4, 5, 8]

# ------------------------------------------------------------
# STEP BY STEP WORKING
# ------------------------------------------------------------

# arr = [4, 3, 1]

# Pivot = 3
# Left  = [1]
# Right = [4]

# Result → [1, 3, 4]

# ------------------------------------------------------------
# IMPORTANT INTERVIEW POINTS
# ------------------------------------------------------------

# - Not stable
# - In-place (traditional version)
# - Very fast in practice
# - Worst case can be avoided using good pivot selection

# ------------------------------------------------------------
# QUICK SUMMARY
# ------------------------------------------------------------

"""
Quick Sort:
- Choose a pivot
- Partition elements
- Sort recursively
- Avg Time: O(n log n)
- Worst: O(n^2)
- Space: O(log n)
"""
