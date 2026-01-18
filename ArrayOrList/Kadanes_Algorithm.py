# ============================================================
# KADANE'S ALGORITHM
# ============================================================

# WHAT:
# Find maximum subarray sum

# WHY:
# - Efficient way to solve max sum problems

# IMPORTANCE:
# - Very famous interview question
# - Optimal solution

# WHEN TO USE:
# - Maximum profit
# - Maximum sum subarray

# TIME:
# O(n)

# SPACE:
# O(1)

print("\n7) Kadane's Algorithm")

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current_sum = arr[0]
max_sum = arr[0]

for x in arr[1:]:
    current_sum = max(x, current_sum + x)
    max_sum = max(max_sum, current_sum)

print("Max subarray sum:", max_sum)
# Output: 6


# ============================================================
# QUICK SUMMARY
# ============================================================

"""
Kadane:
- Tracks current sum
- Resets when sum becomes negative
- Best solution for max subarray sum
"""
