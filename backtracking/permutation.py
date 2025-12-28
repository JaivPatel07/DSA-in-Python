# ============================================================
# PERMUTATION – IMPORTANT NOTES ONLY
# ============================================================

# WHAT:
# Arrangement where ORDER matters

# EXAMPLE:
# [1, 2, 3] →
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]

# WHY BACKTRACKING:
# Try all orders, undo after each try

# KEY IDEA:
# - Choose unused element
# - Add to path
# - When path length == n → one permutation

# TIME COMPLEXITY:
# O(n!)

# SPACE:
# O(n) recursion + path

# ------------------------------------------------------------
# PERMUTATION TEMPLATE
# ------------------------------------------------------------

def permutations(nums):
    result = []

    def backtrack(path):
        # base case
        if len(path) == len(nums):
            result.append(path.copy())
            return

        for num in nums:
            if num in path:
                continue

            path.append(num)     # choose
            backtrack(path)      # explore
            path.pop()           # undo

    backtrack([])
    return result


# ------------------------------------------------------------
# DRIVER CODE
# ------------------------------------------------------------

nums = [1, 2, 3]
print(permutations(nums))

# OUTPUT:
# [
#  [1,2,3], [1,3,2],
#  [2,1,3], [2,3,1],
#  [3,1,2], [3,2,1]
# ]
# ------------------------------------------------------------
# ❌ Time Complexity cannot be reduced below O(n!)
# Because total permutations = n!

# BUT we can OPTIMIZE implementation to reduce overhead


# ------------------------------------------------------------
# OPTIMIZATION 1: USE VISITED ARRAY (FASTER THAN "in path")
# ------------------------------------------------------------

# WHY:
# `if num in path` takes O(n)
# visited[] check is O(1)

def permutations(nums):
    result = []
    n = len(nums)
    visited = [False] * n

    def backtrack(path):
        if len(path) == n:
            result.append(path.copy())
            return

        for i in range(n):
            if visited[i]:
                continue

            visited[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            visited[i] = False

    backtrack([])
    return result


# ------------------------------------------------------------
# OPTIMIZATION 2: IN-PLACE SWAPPING (BEST)
# ------------------------------------------------------------

# WHY:
# - No extra path array
# - No visited array
# - Fastest in practice

def permutations_inplace(nums):
    result = []

    def backtrack(index):
        if index == len(nums):
            result.append(nums.copy())
            return

        for i in range(index, len(nums)):
            nums[index], nums[i] = nums[i], nums[index]  # choose
            backtrack(index + 1)                          # explore
            nums[index], nums[i] = nums[i], nums[index]  # undo

    backtrack(0)
    return result


# ------------------------------------------------------------
# COMPLEXITY COMPARISON
# ------------------------------------------------------------

"""
METHOD                TIME        EXTRA SPACE
--------------------------------------------
Simple (in path)      O(n!*n)     O(n)
Visited array         O(n!)       O(n)
In-place swap         O(n!)       O(1)
"""
