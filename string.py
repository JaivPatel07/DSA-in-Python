# ============================================================
# STRINGS IN PYTHON – BEGINNER FRIENDLY NOTES
# WITH WHY, IMPORTANCE & STEPS
# ============================================================

# String = sequence of characters
s = "hello"


# ============================================================
# 1. STRING TRAVERSAL
# ============================================================

"""
WHAT?
- Visiting each character one by one

WHY?
- To check, count, or modify characters

IMPORTANCE:
- Base of almost all string problems

WHEN TO USE?
- Counting vowels
- Checking characters
"""

print("\n1) String Traversal")

for ch in s:
    print(ch, end=" ")
# Output: h e l l o


# ============================================================
# 2. STRING IMMUTABILITY
# ============================================================

"""
WHAT?
- Strings cannot be changed directly

WHY?
- Strings are immutable for safety & performance

IMPORTANCE:
- Very common interview question

RULE:
- You must create a NEW string
"""

print("\n\n2) Immutability")

s = "hello"
# s[0] = 'H'   ❌ ERROR

s = "H" + s[1:]
print(s)
# Output: Hello


# ============================================================
# 3. STRING REVERSAL
# ============================================================

"""
WHY?
- Used in palindrome & pattern problems

IMPORTANCE:
- Very common interview task
"""

print("\n3) Reverse String")

s = "python"
print(s[::-1])
# Output: nohtyp


# ============================================================
# 4. PALINDROME CHECK
# ============================================================

"""
WHAT?
- String reads same forward & backward

WHY?
- Tests string manipulation

IMPORTANCE:
- Asked in almost every interview
"""

print("\n4) Palindrome Check")

s = "madam"

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Output: Palindrome


# ============================================================
# 5. FREQUENCY COUNT IN STRING (STEP BY STEP)
# ============================================================

"""
WHY?
- Count characters

IMPORTANCE:
- Anagram, duplicates, most frequent char

STEPS:
1. Create empty dictionary
2. Traverse string
3. Increase count
"""

print("\n5) Character Frequency")

s = "banana"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
# Output: {'b': 1, 'a': 3, 'n': 2}


# ============================================================
# 6. ANAGRAM CHECK (STEP BY STEP)
# ============================================================

"""
WHAT?
- Same characters with same frequency

WHY?
- Tests frequency logic

STEPS:
1. Length must be same
2. Count characters
3. Compare counts
"""

print("\n6) Anagram Check")

s1 = "listen"
s2 = "silent"

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")

# Output: Anagram


# ============================================================
# 7. TWO POINTER TECHNIQUE IN STRING
# ============================================================

"""
WHY?
- Avoid extra space
- Efficient comparison

WHEN TO USE?
- Palindrome
- Reverse
"""

print("\n7) Two Pointer")

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


# ============================================================
# 8. SUBSTRING CHECK
# ============================================================

"""
WHY?
- Pattern matching

IMPORTANCE:
- Used in searching problems
"""

print("\n8) Substring Check")

s = "hello world"

print("world" in s)
# Output: True


# ============================================================
# 9. COUNT VOWELS
# ============================================================

"""
WHY?
- Character classification problem

IMPORTANCE:
- Very common beginner question
"""

print("\n9) Count Vowels")

s = "education"
vowels = "aeiou"
count = 0

for ch in s:
    if ch in vowels:
        count += 1

print("Vowel count:", count)
# Output: 5


# ============================================================
# 10. REMOVE DUPLICATES FROM STRING
# ============================================================

"""
WHY?
- Clean data
- Practice sets

IMPORTANCE:
- Interview favorite
"""

print("\n10) Remove Duplicates")

s = "programming"
result = ""

for ch in s:
    if ch not in result:
        result += ch

print(result)
# Output: progamin


# ============================================================
# 11. STRING METHODS (VERY IMPORTANT)
# ============================================================

"""
WHY?
- Built-in methods save time

IMPORTANCE:
- Cleaner & faster code
"""

print("\n11) String Methods")

s = " Hello World "

print(s.lower())     # hello world
print(s.upper())     # HELLO WORLD
print(s.strip())     # Hello World
print(s.replace("World", "Python"))  # Hello Python
print(s.split())     # ['Hello', 'World']


# ============================================================
# FINAL INTERVIEW SUMMARY
# ============================================================

"""
TRAVERSAL        -> Character access
IMMUTABILITY    -> Cannot change directly
REVERSAL        -> s[::-1]
PALINDROME      -> Compare reverse
FREQUENCY       -> Dictionary
ANAGRAM         -> Sorted / frequency
TWO POINTER     -> Efficient compare
SUBSTRING       -> 'in' keyword
"""


# important question

# ============================================================
# LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
# ============================================================

# TECHNIQUE:
# Sliding Window + Set

# WHY WHILE (IMPORTANT):
# Duplicate may still exist after one removal,
# so keep removing until window becomes valid.

# STEPS:
# 1. left = 0, empty set
# 2. Move right pointer
# 3. While s[right] in set:
#    - remove s[left]
#    - left += 1
# 4. Add s[right] to set
# 5. Update max length

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

# ------------------------------------------------------------

s = "abcabcbb"

left = 0
char_set = set()
max_len = 0

for right in range(len(s)):
    while s[right] in char_set:
        char_set.remove(s[left])
        left += 1

    char_set.add(s[right])
    max_len = max(max_len, right - left + 1)

print(max_len)   # 3
