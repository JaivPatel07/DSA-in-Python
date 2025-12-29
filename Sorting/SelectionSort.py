# ============================================================
# SELECTION SORT – BEGINNER FRIENDLY NOTES
# ============================================================

# WHAT IS SELECTION SORT?
# Repeatedly find the smallest element and put it at the correct position.

# IDEA:
# Select minimum element → swap with first unsorted position.

# ------------------------------------------------------------
# WHY NAME "SELECTION"?
# Because we SELECT the smallest element in every pass.

# ------------------------------------------------------------
# WHEN TO USE?
# - For learning sorting logic
# - Not used in real applications (slow)

# ------------------------------------------------------------
# TIME & SPACE COMPLEXITY
# ------------------------------------------------------------
# Best Case   : O(n^2)
# Worst Case  : O(n^2)
# Average     : O(n^2)
# Space       : O(1)

# ------------------------------------------------------------
# BASIC SELECTION SORT CODE
# ------------------------------------------------------------

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i                  # assume current is smallest

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j          # update smallest index

        # swap smallest with current position
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print(arr)   # [11, 12, 22, 25, 64]


# ------------------------------------------------------------
# STEP BY STEP WORKING
# ------------------------------------------------------------

# arr = [64, 25, 12, 22, 11]

# Pass 1:
# smallest = 11 → swap with 64
# [11, 25, 12, 22, 64]

# Pass 2:
# smallest = 12 → swap with 25
# [11, 12, 25, 22, 64]

# Pass 3:
# smallest = 22 → swap with 25
# [11, 12, 22, 25, 64]

# Sorted


# ------------------------------------------------------------
# IMPORTANT INTERVIEW POINTS
# ------------------------------------------------------------

# - Not stable (order of equal elements may change)
# - In-place sorting (no extra memory)
# - Always O(n^2), even if array is sorted
# - Less swaps than Bubble Sort


# ------------------------------------------------------------
# SELECTION vs BUBBLE (VERY IMPORTANT)
# ------------------------------------------------------------

"""
Bubble Sort:
- Many swaps
- Stops early if sorted (optimized)
- Stable

Selection Sort:
- Less swaps
- No early stop
- Not stable
"""


# ------------------------------------------------------------
# QUICK SUMMARY
# ------------------------------------------------------------

"""
Selection Sort:
- Find minimum element
- Place it at correct position
- Time: O(n^2)
- Space: O(1)
- Use only for learning
"""
