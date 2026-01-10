# ============================================================
# REMOVE DUPLICATES FROM STRING
# ============================================================

"""
WHY?
- Clean data
- Practice sets

IMPORTANCE:
- Interview favorite
"""

print("\nRemove Duplicates")

s = "programming"
result = ""

for ch in s:
    if ch not in result:
        result += ch

print(result)
# Output: progamin