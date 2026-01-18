# ============================================================
# SEARCHING – PRACTICE QUESTIONS WITH ANSWERS
# ============================================================


# ------------------------------------------------------------
# Q1. FIND ELEMENT IN ARRAY (LINEAR SEARCH)
# ------------------------------------------------------------
# Input: arr = [4, 2, 7, 1, 9], target = 7
# Output: index = 2

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search([4,2,7,1,9], 7))   # 2


# ------------------------------------------------------------
# Q2. CHECK IF ELEMENT EXISTS (YES / NO)
# ------------------------------------------------------------
# Input: arr = [1,3,5,7], target = 4
# Output: False

def exists(arr, target):
    for x in arr:
        if x == target:
            return True
    return False

print(exists([1,3,5,7], 4))   # False


# ------------------------------------------------------------
# Q3. BINARY SEARCH BASIC
# ------------------------------------------------------------
# Input: arr = [2,4,6,8,10], target = 8
# Output: index = 3

def binary_search(arr, target):
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_search([2,4,6,8,10], 8))   # 3


# ------------------------------------------------------------
# Q4. FIRST OCCURRENCE OF ELEMENT (BINARY SEARCH)
# ------------------------------------------------------------
# Input: arr = [1,2,2,2,3,4], target = 2
# Output: index = 1

def first_occurrence(arr, target):
    left, right = 0, len(arr)-1
    ans = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            ans = mid
            right = mid - 1   # move left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return ans

print(first_occurrence([1,2,2,2,3,4], 2))   # 1


# ------------------------------------------------------------
# Q5. LAST OCCURRENCE OF ELEMENT (BINARY SEARCH)
# ------------------------------------------------------------
# Output: index = 3

def last_occurrence(arr, target):
    left, right = 0, len(arr)-1
    ans = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            ans = mid
            left = mid + 1   # move right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return ans

print(last_occurrence([1,2,2,2,3,4], 2))   # 3


# ------------------------------------------------------------
# Q6. COUNT OCCURRENCES
# ------------------------------------------------------------
# Formula:
# count = last_index - first_index + 1

arr = [1,2,2,2,3,4]
f = first_occurrence(arr, 2)
l = last_occurrence(arr, 2)

count = l - f + 1 if f != -1 else 0
print(count)   # 3


# ------------------------------------------------------------
# Q7. SEARCH INSERT POSITION (BINARY SEARCH)
# ------------------------------------------------------------
# Input: arr = [1,3,5,6], target = 2
# Output: 1

def search_insert(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

print(search_insert([1,3,5,6], 2))   # 1


# ------------------------------------------------------------
# Q8. SEARCH IN SORTED ARRAY (YES / NO)
# ------------------------------------------------------------

def is_present(arr, target):
    return binary_search(arr, target) != -1

print(is_present([2,4,6,8], 6))   # True
print(is_present([2,4,6,8], 7))   # False
