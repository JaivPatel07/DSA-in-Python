# ============================================================
# ANAGRAM CHECK
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

print("\nAnagram Check")

s1 = "listen"
s2 = "silent"

# ------------------------------------------------------------
# METHOD 1: SORTING (O(N log N))
# ------------------------------------------------------------
print("Method 1: Sorting")
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")


# ------------------------------------------------------------
# METHOD 2: FREQUENCY COUNTER (O(N)) - EFFICIENT
# ------------------------------------------------------------
print("\nMethod 2: Frequency Counter (Efficient)")

def check_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    count = {}
    
    for char in s1:
        count[char] = count.get(char, 0) + 1
        
    for char in s2:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] == 0:
            del count[char]
    
    return len(count) == 0

if check_anagram(s1, s2):
    print("Anagram")
else:
    print("Not Anagram")

# Output: Anagram