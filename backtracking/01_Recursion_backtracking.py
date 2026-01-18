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
