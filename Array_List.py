# ============================================================
# ARRAYS / LISTS IN PYTHON
# ============================================================

# WHY ARRAYS?
# Arrays (lists) store multiple values in one variable.
# They are fast, simple, and used in almost EVERY problem.

arr = [1, 2, 3, 4, 5]


# ============================================================
# 1. TRAVERSAL
# ============================================================

"""
WHY?
- To access every element one by one

IMPORTANCE:
- Used in almost every array problem
- Base of searching, counting, updating

WHEN TO USE?
- When you need to visit all elements
"""

print("\n1) Traversal")

for x in arr:
    print(x, end=" ")
# Output: 1 2 3 4 5


# ============================================================
# 2. INSERTION
# ============================================================

"""
WHY?
- To add new elements into array

IMPORTANCE:
- Required when data grows dynamically
- Used in stack, queue, dynamic problems

WHEN TO USE?
- When array size is not fixed
"""

print("\n\n2) Insertion")

arr.append(6)              # insert at end
arr.insert(2, 99)          # insert at index

print(arr)
# Output: [1, 2, 99, 3, 4, 5, 6]


# ============================================================
# 3. DELETION
# ============================================================

"""
WHY?
- To remove unwanted elements

IMPORTANCE:
- Helps reduce memory
- Used in cleanup & optimization problems

WHEN TO USE?
- Remove duplicates
- Delete specific elements
"""

print("\n3) Deletion")

arr.remove(99)     # delete by value
arr.pop()          # delete last element

print(arr)
# Output: [1, 2, 3, 4, 5]


# ============================================================
# 4. PREFIX SUM
# ============================================================

"""
WHY?
- To calculate range sum FAST

IMPORTANCE:
- Avoids repeated sum calculation
- Reduces time from O(n) to O(1)

WHEN TO USE?
- Range sum queries
- Subarray sum problems
"""

print("\n4) Prefix Sum")

nums = [2, 4, 6, 8]
prefix = [0] * len(nums)

prefix[0] = nums[0]
for i in range(1, len(nums)):
    prefix[i] = prefix[i-1] + nums[i]

print("Prefix:", prefix)
# Output: [2, 6, 12, 20]


# ============================================================
# 5. SLIDING WINDOW
# ============================================================

"""
WHY?
- To process subarrays efficiently

IMPORTANCE:
- Saves time from O(n²) to O(n)
- Extremely common in interviews

WHEN TO USE?
- Max/min sum of subarray
- Fixed or variable window problems
"""

print("\n5) Sliding Window")

arr = [2, 1, 5, 1, 3, 2]
k = 3

window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, len(arr)):
    window_sum += arr[i] - arr[i-k]
    max_sum = max(max_sum, window_sum)

print("Max sum:", max_sum)
# Output: 9


# ============================================================
# 6. TWO POINTER TECHNIQUE
# ============================================================

"""
WHY?
- To reduce nested loops

IMPORTANCE:
- Improves performance
- Used with sorted arrays

WHEN TO USE?
- Pair sum
- Reverse array
- Remove duplicates
"""

print("\n6) Two Pointer")

arr = [1, 2, 3, 4, 6]
target = 6

left, right = 0, len(arr)-1

while left < right:
    s = arr[left] + arr[right]
    if s == target:
        print("Pair:", arr[left], arr[right])
        break
    elif s < target:
        left += 1
    else:
        right -= 1


# ============================================================
# 7. KADANE'S ALGORITHM
# ============================================================

"""
WHY?
- To find maximum subarray sum

IMPORTANCE:
- Famous interview algorithm
- Optimal solution O(n)

WHEN TO USE?
- Max profit
- Max sum problems
"""

print("\n7) Kadane's Algorithm")

arr = [-2,1,-3,4,-1,2,1,-5,4]

current = max_sum = arr[0]

for x in arr[1:]:
    current = max(x, current + x)
    max_sum = max(max_sum, current)

print("Max subarray sum:", max_sum)
# Output: 6


# ============================================================
# 8. FREQUENCY COUNT
# ============================================================

"""
WHY?
- To count occurrences

IMPORTANCE:
- Used in majority element
- Anagram & duplicate problems

WHEN TO USE?
- Counting
- Matching frequencies
"""

print("\n8) Frequency Count")

arr = [1,2,2,3,1,1]
freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1

print(freq)
# Output: {1: 3, 2: 2, 3: 1}


# ============================================================
# 9. COMMON INTERVIEW TRICKS
# ============================================================

"""
WHY?
- Shortcuts save time

IMPORTANCE:
- Cleaner code
- Faster solutions
"""

print("\n9) Tricks")

arr = [1,2,3,4]
print("Reverse:", arr[::-1])
# Output: [4,3,2,1]

print("Sorted:", arr == sorted(arr))
# Output: True


# ============================================================
# FINAL INTERVIEW SUMMARY
# ============================================================

"""
TRAVERSAL       -> Access elements
INSERTION       -> Add data
DELETION        -> Remove data
PREFIX SUM      -> Fast range sum
SLIDING WINDOW  -> Subarray problems
TWO POINTER     -> Optimize loops
KADANE          -> Max subarray
FREQUENCY MAP   -> Counting problems
"""
