# ============================================================
# COMBINATION – IMPORTANT NOTES ONLY
# ============================================================

# WHAT:
# Selection where ORDER does NOT matter

# EXAMPLE:
# nums = [1, 2, 3]
# combinations →
# [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]

# PERMUTATION vs COMBINATION:
# Permutation -> order matters
# Combination -> order does NOT matter

# WHY BACKTRACKING:
# Explore all possible selections

# KEY IDEA:
# - Use start index
# - Move forward only (avoid reusing previous elements)

# TIME COMPLEXITY:
# O(2^n)

# SPACE:
# O(n)

# ------------------------------------------------------------
# COMBINATION TEMPLATE (IMPORTANT)
# ------------------------------------------------------------

def combinations(nums):
    result = []

    def backtrack(start, path):
        result.append(path.copy())

        for i in range(start, len(nums)):
            path.append(nums[i])      # choose
            backtrack(i + 1, path)    # explore
            path.pop()                # undo

    backtrack(0, [])
    return result


# ------------------------------------------------------------
# DRIVER CODE
# ------------------------------------------------------------

nums = [1, 2, 3]
print(combinations(nums))

# OUTPUT:
# [
#  [], [1], [1,2], [1,2,3],
#  [1,3], [2], [2,3], [3]
# ]
