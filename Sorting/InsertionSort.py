# ============================================================
# INSERTION SORT – BEGINNER FRIENDLY NOTES
# ============================================================

# WHAT IS INSERTION SORT?
# Insertion Sort builds the sorted array one element at a time.
# It takes one element and inserts it into its correct position
# in the already sorted part of the array.

# ------------------------------------------------------------
# REAL LIFE EXAMPLE (VERY IMPORTANT)
# ------------------------------------------------------------
# Imagine you are playing cards.
# You pick one card at a time and insert it in the correct place
# among the cards already in your hand (sorted).
#
# Example:
# Hand: [2, 5, 9]
# New card: 4
# Insert 4 between 2 and 5 → [2, 4, 5, 9]
#
# This is exactly how Insertion Sort works.

# ------------------------------------------------------------
# WHEN TO USE?
# ------------------------------------------------------------
# - Small datasets
# - Nearly sorted arrays
# - Learning sorting fundamentals

# ------------------------------------------------------------
# TIME & SPACE COMPLEXITY
# ------------------------------------------------------------
# Best Case   : O(n)    (already sorted)
# Worst Case  : O(n^2)
# Average     : O(n^2)
# Space       : O(1)

# ------------------------------------------------------------
# BASIC INSERTION SORT CODE
# ------------------------------------------------------------

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):        # start from second element
        key = arr[i]             # element to be inserted
        j = i - 1

        # shift elements greater than key to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # place key at correct position
        arr[j + 1] = key

arr = [5, 3, 8, 4, 2]
insertion_sort(arr)
print(arr)   # [2, 3, 4, 5, 8]

# ------------------------------------------------------------
# STEP BY STEP WORKING (SMALL EXAMPLE)
# ------------------------------------------------------------

# arr = [4, 3, 1]

# Pass 1 (i = 1):
# key = 3
# Compare with 4 → shift 4
# Insert 3 → [3, 4, 1]

# Pass 2 (i = 2):
# key = 1
# Compare with 4 → shift
# Compare with 3 → shift
# Insert 1 → [1, 3, 4]

# Sorted

# ------------------------------------------------------------
# IMPORTANT INTERVIEW POINTS
# ------------------------------------------------------------

# - Stable sort (keeps order of equal elements)
# - In-place sorting (no extra memory)
# - Very efficient for small or nearly sorted arrays
# - Slower for large unsorted data

# ------------------------------------------------------------
# WHEN NOT TO USE INSERTION SORT?
# ------------------------------------------------------------

# - Large arrays with random order
# - Time-critical applications

# ------------------------------------------------------------
# QUICK SUMMARY
# ------------------------------------------------------------

"""
Insertion Sort:
- Insert elements into their correct position
- Works like sorting playing cards
- Best case: O(n)
- Worst case: O(n^2)
- Space: O(1)
- Good for small or nearly sorted arrays
"""
