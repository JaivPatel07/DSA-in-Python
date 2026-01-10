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