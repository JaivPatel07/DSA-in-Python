# ============================================================
# FREQUENCY COUNT IN STRING
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

print("\nCharacter Frequency")

s = "banana"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
# Output: {'b': 1, 'a': 3, 'n': 2}