# ============================================================
# FREQUENCY COUNT
# ============================================================

# WHAT:
# Count how many times each element appears

# WHY:
# - To know occurrence of elements

# IMPORTANCE:
# - Majority element problems
# - Duplicate detection
# - Anagram checking

# WHEN TO USE:
# - Counting items
# - Matching frequencies

# TIME:
# O(n)

# SPACE:
# O(n)

print("\n8) Frequency Count")

arr = [1, 2, 2, 3, 1, 1]
freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1

print(freq)
# Output: {1: 3, 2: 2, 3: 1}


# ============================================================
# QUICK SUMMARY
# ============================================================

"""
Frequency Count:
- Uses dictionary
- Fast counting
- Common interview pattern
"""
