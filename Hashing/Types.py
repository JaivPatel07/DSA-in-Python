"""
============================================================
HASHING IN PYTHON
============================================================

This file explains:
1. What hashing is
2. What collision is
3. Probing methods (Linear, Quadratic, Double Hashing)
4. WHY each probing method is useful

------------------------------------------------------------
WHAT IS HASHING?
------------------------------------------------------------
Hashing is a technique to store and search data FAST.
It uses a hash function to convert a key into an index.

Example:
    index = key % table_size

Average Time Complexity:
    Insert  : O(1)
    Search  : O(1)
    Delete  : O(1)

------------------------------------------------------------
WHAT IS COLLISION?
------------------------------------------------------------
Collision happens when two keys give the SAME index.

Example:
    hash(10) = 0
    hash(20) = 0   ← collision

To handle collision, we use PROBING METHODS.

============================================================
PROBING METHODS (OPEN ADDRESSING)
============================================================

------------------------------------------------------------
1. LINEAR PROBING
------------------------------------------------------------
Formula:
    index = (hash(key) + i) % size

HOW IT WORKS:
- If the position is full, move to the NEXT index
- Check one by one

WHY USE IT?
✔ Very easy to understand
✔ Simple implementation

PROBLEM:
❌ Primary clustering (many keys stick together)

------------------------------------------------------------
2. QUADRATIC PROBING
------------------------------------------------------------
Formula:
    index = (hash(key) + i*i) % size

HOW IT WORKS:
- Instead of checking next index, jump using squares
- Jumps: 1, 4, 9, 16 ...

WHY USE IT?
✔ Reduces clustering
✔ Better than linear probing

PROBLEM:
❌ Secondary clustering still possible

------------------------------------------------------------
3. DOUBLE HASHING
------------------------------------------------------------
Formula:
    index = (hash1(key) + i * hash2(key)) % size

HOW IT WORKS:
- Uses TWO hash functions
- Second hash decides jump size

WHY USE IT?
✔ Best distribution
✔ Least collisions
✔ Used in real systems

============================================================
CODE IMPLEMENTATION
============================================================
"""

# -----------------------------------------------------------
# SIMPLE HASH FUNCTION
# -----------------------------------------------------------
def hash_function(key, size):
    return key % size


# -----------------------------------------------------------
# HASH TABLE WITH LINEAR PROBING
# -----------------------------------------------------------
class HashTableLinearProbing:
    """
    LINEAR PROBING
    WHY USE:
    - Simple
    - Beginner friendly
    """
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def insert(self, key):
        index = hash_function(key, self.size)
        while self.table[index] is not None:
            index = (index + 1) % self.size
        self.table[index] = key

    def display(self):
        print("Linear Probing Table:")
        print(self.table)


# -----------------------------------------------------------
# HASH TABLE WITH QUADRATIC PROBING
# -----------------------------------------------------------
class HashTableQuadraticProbing:
    """
    QUADRATIC PROBING
    WHY USE:
    - Reduces clustering
    - Better than linear probing
    """
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def insert(self, key):
        index = hash_function(key, self.size)
        i = 1
        while self.table[index] is not None:
            index = (hash_function(key, self.size) + i * i) % self.size
            i += 1
        self.table[index] = key

    def display(self):
        print("Quadratic Probing Table:")
        print(self.table)


# -----------------------------------------------------------
# HASH TABLE WITH DOUBLE HASHING
# -----------------------------------------------------------
class HashTableDoubleHashing:
    """
    DOUBLE HASHING
    WHY USE:
    - Best performance
    - Least collision
    - Used in real applications
    """
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash1(self, key):
        return key % self.size

    def hash2(self, key):
        return 1 + (key % (self.size - 1))

    def insert(self, key):
        index = self.hash1(key)
        i = 0
        while self.table[index] is not None:
            index = (self.hash1(key) + i * self.hash2(key)) % self.size
            i += 1
        self.table[index] = key

    def display(self):
        print("Double Hashing Table:")
        print(self.table)


# -----------------------------------------------------------
# DRIVER CODE (RUN & SEE OUTPUT)
# -----------------------------------------------------------
if __name__ == "__main__":
    keys = [10, 20, 30, 40]

    lp = HashTableLinearProbing(7)
    for k in keys:
        lp.insert(k)
    lp.display()

    qp = HashTableQuadraticProbing(7)
    for k in keys:
        qp.insert(k)
    qp.display()

    dh = HashTableDoubleHashing(7)
    for k in keys:
        dh.insert(k)
    dh.display()

"""
============================================================
FINAL SUMMARY (EXAM READY)
============================================================
Linear Probing  : Simple but causes clustering
Quadratic      : Better distribution than linear
Double Hashing : Best method, minimum collision

Use Double Hashing in real-world applications.
============================================================
"""