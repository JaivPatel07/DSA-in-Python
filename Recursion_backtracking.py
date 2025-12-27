# ============================================================
# RECURSION & BACKTRACKING – IMPORTANT NOTES ONLY
# ============================================================

# ------------------------------------------------------------
# RECURSION
# ------------------------------------------------------------

# WHAT:
# Function calling itself

# MUST HAVE:
# 1. Base Case  -> stops recursion
# 2. Recursive Case -> moves towards base case

# WHY:
# Solves problems that can be broken into smaller subproblems

# WHEN TO USE:
# - Tree problems
# - Divide & conquer
# - DFS
# - Mathematical problems

# COMMON MISTAKES:
# - Missing base case
# - Not changing input

# TIME:
# Depends on recursion depth

# ------------------------------------------------------------
# BASIC RECURSION EXAMPLE
# ------------------------------------------------------------

def factorial(n):
    if n == 0:          # base case
        return 1
    return n * factorial(n-1)

print(factorial(5))     # 120


# ------------------------------------------------------------
# PRINT 1 TO N (RECURSION THINKING)
# ------------------------------------------------------------

def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n-1)
    print(n)

print_1_to_n(5)
# 1 2 3 4 5


# ------------------------------------------------------------
# BACKTRACKING
# ------------------------------------------------------------

# WHAT:
# Try → Explore → Undo → Try next

# WHY:
# Explore all possibilities

# KEY IDEA:
# After recursive call → undo changes

# WHEN TO USE:
# - Permutations
# - Combinations
# - Subsets
# - N-Queens
# - Sudoku

# COMMON LINE:
# path.pop()   # undo step

# ------------------------------------------------------------
# BACKTRACKING TEMPLATE (IMPORTANT)
# ------------------------------------------------------------

# def backtrack(path, choices):
#     if base_condition:
#         answer.append(path.copy())
#         return

#     for choice in choices:
#         path.append(choice)     # choose
#         backtrack(path, choices) # explore
#         path.pop()              # undo


# ------------------------------------------------------------
# SUBSETS (BACKTRACKING)
# ------------------------------------------------------------

def subsets(nums):
    result = []

    def backtrack(start, path):
        result.append(path.copy())

        for i in range(start, len(nums)):
            path.append(nums[i])      # choose
            backtrack(i+1, path)      # explore
            path.pop()                # undo

    backtrack(0, [])
    return result

print(subsets([1, 2, 3]))
# [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]


# ------------------------------------------------------------
# PERMUTATIONS (BACKTRACKING)
# ------------------------------------------------------------

def permutations(nums):
    result = []

    def backtrack(path):
        if len(path) == len(nums):
            result.append(path.copy())
            return

        for num in nums:
            if num in path:
                continue
            path.append(num)      # choose
            backtrack(path)       # explore
            path.pop()             # undo

    backtrack([])
    return result

print(permutations([1, 2, 3]))
# [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]


# ------------------------------------------------------------
# INTERVIEW QUICK RULES
# ------------------------------------------------------------

"""
RECURSION:
- Always define base case first
- Think: smaller problem

BACKTRACKING:
- Choose → Explore → Undo
- Use path.copy()
- Undo is MUST

IF STUCK:
- Write recursion tree
"""
