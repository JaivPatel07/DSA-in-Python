# ============================================================
# ARRAY OPERATIONS
# ============================================================

arr = [1, 2, 3, 4, 5]


# ============================================================
# 1. TRAVERSAL
# ============================================================

# WHAT:
# Visit each element one by one

# WHY:
# - To read / print / update elements

# IMPORTANCE:
# - Base of searching, sorting, counting
# - Used in almost every array problem

# TIME:
# O(n)

print("\n1) Traversal")

for x in arr:
    print(x, end=" ")
# Output: 1 2 3 4 5


# ============================================================
# 2. INSERTION
# ============================================================

# WHAT:
# Add new element to array

# WHY:
# - Data grows dynamically

# IMPORTANCE:
# - Used in stack, queue, real-life lists

# METHODS:
# append() → add at end
# insert() → add at specific index

# TIME:
# append → O(1)
# insert → O(n)

print("\n\n2) Insertion")

arr.append(6)          # insert at end
arr.insert(2, 99)      # insert at index 2

print(arr)
# Output: [1, 2, 99, 3, 4, 5, 6]


# ============================================================
# 3. DELETION
# ============================================================

# WHAT:
# Remove element from array

# WHY:
# - Remove unwanted data

# IMPORTANCE:
# - Memory optimization
# - Used in filtering problems

# METHODS:
# remove() → delete by value
# pop()    → delete by index / last element

# TIME:
# O(n)

print("\n3) Deletion")

arr.remove(99)     # delete value 99
arr.pop()          # delete last element

print(arr)
# Output: [1, 2, 3, 4, 5]


# ============================================================
# QUICK SUMMARY
# ============================================================

"""
Traversal → Visit elements → O(n)
Insertion → Add element     → O(1) / O(n)
Deletion  → Remove element  → O(n)
"""
