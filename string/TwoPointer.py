# ============================================================
# TWO POINTER TECHNIQUE IN STRING
# ============================================================

"""
WHY?
- Avoid extra space
- Efficient comparison

WHEN TO USE?
- Palindrome
- Reverse
"""

print("\nTwo Pointer")

s = "level"
left, right = 0, len(s) - 1
flag = True

while left < right:
    if s[left] != s[right]:
        flag = False
        break
    left += 1
    right -= 1

print("Palindrome:", flag)
# Output: True