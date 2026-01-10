# ============================================================
# STRINGS BASICS – BEGINNER FRIENDLY NOTES
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
# 3. SUBSTRING CHECK
# ============================================================
"""
WHY?
- Pattern matching

IMPORTANCE:
- Used in searching problems
"""
print("\n3) Substring Check")

s = "hello world"

print("world" in s)
# Output: True


# ============================================================
# 4. STRING METHODS (VERY IMPORTANT)
# ============================================================
"""
WHY?
- Built-in methods save time

IMPORTANCE:
- Cleaner & faster code
"""
print("\n4) String Methods")

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
SUBSTRING       -> 'in' keyword
METHODS         -> Use built-ins for speed
"""