# ============================================================
# PREFIX SUM 
# ============================================================

# WHAT:
# Precompute cumulative sums

# WHY:
# - Get range sum quickly

# IMPORTANCE:
# - Avoid repeated addition
# - Speeds up subarray problems

# WHEN TO USE:
# - Range sum queries
# - Subarray sum problems

# TIME:
# Build → O(n)
# Query → O(1)

# SPACE:
# O(n)

print("\n4) Prefix Sum")

nums = [2, 4, 6, 8]
prefix = [0] * len(nums)

prefix[0] = nums[0]
for i in range(1, len(nums)):
    prefix[i] = prefix[i - 1] + nums[i]

print("Prefix:", prefix)
# Output: [2, 6, 12, 20]


# ============================================================
# QUICK SUMMARY
# ============================================================

"""
Prefix Sum:
- Store cumulative sums
- Fast range queries
- Very common interview pattern
"""
