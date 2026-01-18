# ============================================================
# SLIDING WINDOW
# ============================================================

# WHAT:
# Process subarrays using a moving window

# WHY:
# - Avoid nested loops

# IMPORTANCE:
# - Reduces time complexity
# - Very common interview pattern

# WHEN TO USE:
# - Fixed size subarray problems
# - Maximum / minimum sum

# TIME:
# O(n)

# SPACE:
# O(1)

print("\n5) Sliding Window")

arr = [2, 1, 5, 1, 3, 2]
k = 3

window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, len(arr)):
    window_sum += arr[i] - arr[i - k]
    max_sum = max(max_sum, window_sum)

print("Max sum:", max_sum)
# Output: 9


# ============================================================
# QUICK SUMMARY
# ============================================================

"""
Sliding Window:
- Move window instead of recompute
- Converts O(n²) → O(n)
- Best for subarray problems
"""
