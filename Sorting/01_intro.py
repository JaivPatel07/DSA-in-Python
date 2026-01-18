# ============================================================
# SORTING – BEGINNER FRIENDLY NOTES
# ============================================================

# SORTING:
# Arranging elements in ascending / descending order

# WHY SORTING?
# - Makes searching faster
# - Helps in duplicate handling
# - Used in many algorithms

# ------------------------------------------------------------
# TYPES OF SORTING
# ------------------------------------------------------------

# 1. Bubble Sort
# 2. Selection Sort
# 3. Insertion Sort
# 4. Merge Sort
# 5. Quick Sort
# 6. Python Built-in Sort

# ============================================================
# SORTING COMPARISON (INTERVIEW)
# ============================================================

"""
SORT          TIME (AVG)      SPACE
-----------------------------------
Bubble        O(n²)           O(1)
Selection     O(n²)           O(1)
Insertion     O(n²)           O(1)
Merge         O(n log n)      O(n)
Quick         O(n log n)      O(log n)
Python sort   O(n log n)      O(n)
"""


# ============================================================
# WHEN TO USE WHAT?
# ============================================================

"""
Small array        → Insertion / Bubble
Large array        → Merge / Quick
Stable sort needed → Merge
Fast & simple      → Python sort
"""
