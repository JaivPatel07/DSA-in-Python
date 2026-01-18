# ============================================================
# COUNT VOWELS
# ============================================================

"""
WHY?
- Character classification problem

IMPORTANCE:
- Very common beginner question
"""

print("\nCount Vowels")

s = "education"
vowels = "aeiou"
count = 0

for ch in s:
    if ch in vowels:
        count += 1

print("Vowel count:", count)
# Output: 5