# ============================================================
# PALINDROME CHECK
# ============================================================

"""
WHAT?
- String reads same forward & backward

WHY?
- Tests string manipulation

IMPORTANCE:
- Asked in almost every interview
"""

print("\nPalindrome Check")

s = "madam"

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Output: Palindrome