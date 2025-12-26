# ============================================================
# TIME & SPACE COMPLEXITY (EASY GUIDE)
# ============================================================

# ------------------------------------------------------------
# WHAT IS TIME COMPLEXITY?
# ------------------------------------------------------------
# Imagine you are baking cookies. 🍪
# Time Complexity asks: "If I bake MORE cookies, how much longer does it take?"
#
# It is NOT about seconds or minutes.
# It is about GROWTH.
#
# - 1 cookie takes 5 mins.
# - 100 cookies take 500 mins? (Linear)
# - or 100 cookies still take 5 mins? (Constant)
#
# WHY LEARN THIS?
# ✅ To write code that doesn't crash with big data.
# ✅ To pass coding interviews.


# ------------------------------------------------------------
# BIG-O NOTATION (THE SCORECARD)
# ------------------------------------------------------------
# Big-O is just a label for how fast/slow code is.
# We usually look at the WORST case (if everything goes wrong).
#
# Common Labels (Fastest to Slowest):
# 1. O(1)    → Instant (Best)
# 2. O(log n)→ Very Fast
# 3. O(n)    → Fair (Linear)
# 4. O(n^2)  → Slow (Quadratic)
# 5. O(2^n)  → Very Slow (Exponential)


# ------------------------------------------------------------
# 1. O(1) – CONSTANT TIME (INSTANT)
# ------------------------------------------------------------
# No matter how much data, time stays the SAME.

def get_first_item(items):
    return items[0]

print(get_first_item([10, 20, 30, 40, 50]))
# Output: 10

# EXPLANATION:
# - Whether the list has 3 items or 1 million items,
#   getting the first one takes 1 step.
# - This is the BEST speed.


# ------------------------------------------------------------
# 2. O(n) – LINEAR TIME (FAIR)
# ------------------------------------------------------------
# More data = More time.
# 10 items = 10 steps.
# 100 items = 100 steps.

def print_all(items):
    for item in items:
        print(item)

print_all([1, 2, 3])

# EXPLANATION:
# - We have to visit EVERY item once.
# - If list size doubles, time doubles.


# ------------------------------------------------------------
# 3. O(n^2) – QUADRATIC TIME (SLOW)
# ------------------------------------------------------------
# Usually happens with "Loop inside a Loop".
# For every item, we check every other item.

def print_pairs(items):
    for x in items:          # Outer loop
        for y in items:      # Inner loop
            print(x, y)

print_pairs([1, 2])
# Output:
# 1 1
# 1 2
# 2 1
# 2 2

# EXPLANATION:
# - If list has 10 items, we do 10 * 10 = 100 steps.
# - If list has 100 items, we do 100 * 100 = 10,000 steps!
# - Avoid this for large data.


# ------------------------------------------------------------
# 4. O(log n) – LOGARITHMIC TIME (SUPER FAST)
# ------------------------------------------------------------
# Imagine looking for a word in a dictionary.
# You don't read every page. You open the middle, see if it's left or right.
# You cut the problem in HALF every time.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # Find middle
        
        if arr[mid] == target:
            return True            # Found it!
        elif arr[mid] < target:
            left = mid + 1         # Look in right half
        else:
            right = mid - 1        # Look in left half
            
    return False

print(binary_search([1, 2, 3, 4, 5], 4))
# Output: True

# EXPLANATION:
# - Even with 1 million items, it only takes about 20 steps.
# - Very efficient.


# ------------------------------------------------------------
# 5. O(2^n) – EXPONENTIAL TIME (TOO SLOW)
# ------------------------------------------------------------
# Every new item DOUBLES the work.
# Often happens in recursion if not careful.

def fib_recursive(n):
    if n <= 1: return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# EXPLANATION:
# - The computer calculates the same things over and over.
# - Avoid unless n is very small.


# ------------------------------------------------------------
# WHAT IS SPACE COMPLEXITY?
# ------------------------------------------------------------
# Time Complexity = How much TIME.
# Space Complexity = How much MEMORY (RAM).
#
# Does your code need to create a new list?
# Does it need to remember a lot of things?


# ------------------------------------------------------------
# SPACE EXAMPLES
# ------------------------------------------------------------

# O(1) Space (Good)
def add_numbers(a, b):
    return a + b
# We only use 2 variables. Memory usage doesn't grow.


# O(n) Space (Heavy)
def copy_list(items):
    new_list = []
    for item in items:
        new_list.append(item)
    return new_list
# If input is 1000 items, we create a NEW list of 1000 items.
# More input = More memory needed.


# ------------------------------------------------------------
# REAL-LIFE ANALOGY (CLASSROOM)
# ------------------------------------------------------------
# Scenario: Teacher checking homework.
#
# O(1): Teacher looks at the first student only. (Instant)
# O(n): Teacher checks every student one by one. (Fair)
# O(n^2): Every student checks every other student's paper. (Chaos/Slow)
#
# Space Complexity:
# O(1): Teacher writes grades on the blackboard (Fixed space).
# O(n): Teacher uses a new sheet of paper for every student (More students = More paper).


# ------------------------------------------------------------
# SUMMARY FOR INTERVIEWS
# ------------------------------------------------------------
# 1. Big-O measures how code slows down as data grows.
# 2. O(1) is best. O(n^2) is slow.
# 3. Loops usually mean O(n).
# 4. Nested loops (loop inside loop) usually mean O(n^2).
# 5. Halving the data (binary search) is O(log n).
# 6. Don't forget Memory (Space Complexity)!

# ===================== END OF FILE ==========================
