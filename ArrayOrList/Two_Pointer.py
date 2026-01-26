# ============================================================
# 6. TWO POINTER TECHNIQUE – BEGINNER FRIENDLY NOTES
# ============================================================

# WHAT:
# Use two pointers to traverse array from both ends

# WHY:
# - Reduce nested loops
# - Solve problems efficiently

# IMPORTANCE:
# - Improves performance
# - Common in sorted arrays

# WHEN TO USE:
# - Pair sum problems
# - Reverse array
# - Remove duplicates
# - Subarray sum problems

# TIME:
# O(n)

# SPACE:
# O(1)

print("\n6) Two Pointer")

arr = [1, 2, 3, 4, 6]
target = 6

left, right = 0, len(arr) - 1

while left < right:
    s = arr[left] + arr[right]
    if s == target:
        print("Pair:", arr[left], arr[right])
        break
    elif s < target:
        left += 1
    else:
        right -= 1
# Output: Pair: 2 4


# ============================================================
# ADDITIONAL USES
# ============================================================

# 1) Reverse array in-place
arr2 = [1,2,3,4]
l, r = 0, len(arr2)-1
while l < r:
    arr2[l], arr2[r] = arr2[r], arr2[l]
    l += 1
    r -= 1
print("Reversed:", arr2)
# Output: [4,3,2,1]

# 2) Remove duplicates from sorted array
arr3 = [1,1,2,2,3]
res = []
for r in range(len(arr3)):
    if r == 0 or arr3[r] != arr3[r-1]:
        res.append(arr3[r])
print("No duplicates:", res)
# Output: [1,2,3]
# ============================================================