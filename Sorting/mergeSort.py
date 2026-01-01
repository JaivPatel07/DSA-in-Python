# ============================================================
# MERGE SORT – BEGINNER FRIENDLY NOTES
# ============================================================

# WHAT IS MERGE SORT?
# Merge Sort is a Divide and Conquer algorithm.
# It divides the array into smaller parts, sorts them,
# and then merges them back together.

# ------------------------------------------------------------
# REAL LIFE EXAMPLE
# ------------------------------------------------------------
# Imagine you have two already sorted piles of books.
# You compare the top book of both piles and pick the smaller one.
# Keep doing this until all books are merged in sorted order.
# This merging idea is Merge Sort.

# ------------------------------------------------------------
# WHEN TO USE?
# ------------------------------------------------------------
# - Large datasets
# - When stable sorting is required
# - When guaranteed performance is needed

# ------------------------------------------------------------
# TIME & SPACE COMPLEXITY
# ------------------------------------------------------------
# Best Case   : O(n log n)
# Worst Case  : O(n log n)
# Average     : O(n log n)
# Space       : O(n)   (extra memory)

# ------------------------------------------------------------
# MERGE SORT CODE
# ------------------------------------------------------------

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = [5, 3, 8, 4, 2]
arr = merge_sort(arr)
print(arr)   # [2, 3, 4, 5, 8]

# ------------------------------------------------------------
# STEP BY STEP WORKING
# ------------------------------------------------------------

# arr = [4, 3, 1, 2]

# Divide:
# [4, 3]   [1, 2]
# [4] [3]  [1] [2]

# Merge:
# [3,4]    [1,2]
# Final → [1,2,3,4]

# ------------------------------------------------------------
# IMPORTANT INTERVIEW POINTS
# ------------------------------------------------------------

# - Stable sort
# - Not in-place (needs extra memory)
# - Very fast and reliable
# - Used in real applications

# ------------------------------------------------------------
# QUICK SUMMARY
# ------------------------------------------------------------

"""
Merge Sort:
- Divide array into halves
- Sort recursively
- Merge sorted halves
- Time: O(n log n)
- Space: O(n)
"""
