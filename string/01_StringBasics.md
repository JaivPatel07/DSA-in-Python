# String – Complete Notes (DSA & Python)

---

## 📌 What is a String?

A **string** is a sequence of characters enclosed in quotes.

Examples:

```python
s1 = "hello"
s2 = 'world'
```

Strings are:

* ✅ **Immutable** (cannot be changed in-place)
* ✅ Ordered
* ✅ Iterable

---

## 🔹 String Representation

Characters are stored as **ASCII / Unicode values**.

Example:

```python
ord('A')   # 65
chr(97)    # 'a'
```

---

## 1️⃣ Basic String Operations

```python
s = "python"
len(s)        # 6
s[0]          # 'p'
s[-1]         # 'n'
```

---

## 2️⃣ String Slicing (Very Important ⭐⭐)

```python
s = "programming"

s[0:4]    # 'prog'
s[2:]     # 'ogramming'
s[:5]     # 'progr'
s[::-1]   # reverse string
```

---

## 3️⃣ String Immutability (Tricky ⚠️)

```python
s = "hello"
# s[0] = 'H'  ❌ Error

s = 'H' + s[1:]   # ✅ Correct
```

---

## 4️⃣ Common String Methods (with Output & Explanation)

```python
s = "Hello World"
```

| Method  | Code                          | Output              | What it does             |
| ------- | ----------------------------- | ------------------- | ------------------------ |
| lower   | `s.lower()`                   | `'hello world'`     | Converts to lowercase    |
| upper   | `s.upper()`                   | `'HELLO WORLD'`     | Converts to uppercase    |
| title   | `s.title()`                   | `'Hello World'`     | Capitalizes each word    |
| strip   | `s.strip()`                   | `'Hello World'`     | Removes spaces from ends |
| replace | `s.replace('World','Python')` | `'Hello Python'`    | Replaces substring       |
| split   | `s.split()`                   | `['Hello','World']` | Splits into list         |

---

## 5️⃣ String Checking Methods (with Output)

```python
s = "Hello123"
```

| Method     | Code                | Output  | Meaning                 |
| ---------- | ------------------- | ------- | ----------------------- |
| isalpha    | `s.isalpha()`       | `False` | Only letters            |
| isdigit    | `s.isdigit()`       | `False` | Only digits             |
| isalnum    | `s.isalnum()`       | `True`  | Letters + digits        |
| startswith | `s.startswith('H')` | `True`  | Starts with given value |
| endswith   | `s.endswith('3')`   | `True`  | Ends with given value   |

---

## 6️⃣ String Concatenation

```python
s1 = "Hello"
s2 = "World"

s1 + " " + s2
" ".join([s1, s2])
```

---

## 7️⃣ String Formatting (with Output)

```python
name = "Alex"
age = 20
```

### Old Style

```python
"Hello %s" % name
```

Output:

```
Hello Alex
```

### format()

```python
"{} is {} years old".format(name, age)
```

Output:

```
Alex is 20 years old
```

### f-strings ⭐

```python
f"{name} is {age} years old"
```

Output:

```
Alex is 20 years old
```

---

## 8️⃣ Looping Through String

```python
for ch in "abc":
    print(ch)
```

---

## 9️⃣ String Comparison

```python
"abc" == "abc"   # True
"abc" < "abd"    # True (lexicographical)
```

---

## 🔟 Important String Problems (with Output)

### 🔹 Reverse a String

```python
s = "python"
s[::-1]
```

Output:

```
nohtyp
```

---

### 🔹 Check Palindrome

```python
s = "madam"
s == s[::-1]
```

Output:

```
True
```

---

### 🔹 Count Frequency of Characters

```python
from collections import Counter
Counter("banana")
```

Output:

```
{'a': 3, 'b': 1, 'n': 2}
```

---

## 1️⃣1️⃣ Substring Search (with Output)

### Using `in`

```python
"py" in "python"
```

Output:

```
True
```

---

### Using `find()`

```python
"python".find("tho")
```

Output:

```
-1
```

`-1` means substring not found

---

## 1️⃣2️⃣ String to List & Vice Versa

```python
s = "a,b,c"
arr = s.split(',')

"-".join(arr)
```

---

## ⚠️ Common Mistakes

* Trying to modify string directly ❌
* Forgetting strings are immutable ❌
* Using `+` repeatedly in loops (slow) ❌

---

## 🎯 Real-Life Examples

* Password validation
* Text search
* Chat applications
* DNA sequence analysis

---

## 📌 Interview Tips

* Always mention **immutability**
* Know slicing & frequency problems
* Be clear on time complexity

---

## 📊 Time Complexity Notes

* Access by index → `O(1)`
* Slicing → `O(n)`
* Concatenation → `O(n)`

---
