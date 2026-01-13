# 🌳 Tree Data Structure – Complete Notes

## 1. What is a Tree?

A **tree** is a **non-linear data structure** that represents data in a **hierarchical** manner. It consists of **nodes** connected by **edges**, with one node designated as the **root**.

Unlike arrays or linked lists, trees allow efficient representation of relationships such as parent–child.

---

## 2. Basic Terminology

* **Node**: A basic unit containing data
* **Root**: Topmost node of the tree
* **Parent**: A node that has children
* **Child**: A node that descends from a parent
* **Leaf (External Node)**: Node with no children
* **Internal Node**: Node with at least one child
* **Edge**: Connection between two nodes
* **Sibling**: Nodes with the same parent
* **Ancestor**: All parents of a node up to the root
* **Descendant**: All children of a node
* **Degree**: Number of children of a node
* **Depth**: Number of edges from root to a node
* **Height**: Number of edges on the longest path from node to a leaf
* **Level**: Depth + 1

---

## 3. Properties of Trees

* A tree with **N nodes** has **N − 1 edges**
* There is **exactly one path** between any two nodes
* Trees are **acyclic** (no loops)

---

## 4. Types of Trees

### 4.1 General Tree

* A node can have any number of children

### 4.2 Binary Tree

* Each node has **at most two children**
* Children are referred to as **left** and **right**

#### Types of Binary Trees

* **Full Binary Tree**: Every node has 0 or 2 children
* **Perfect Binary Tree**: All internal nodes have 2 children and all leaves are at the same level
* **Complete Binary Tree**: All levels are filled except possibly the last (filled from left)
* **Skewed Binary Tree**: Every node has only one child

---

### 4.3 Binary Search Tree (BST)

A binary tree with the property:

* Left subtree contains values **less than root**
* Right subtree contains values **greater than root**

**Inorder traversal of BST gives sorted order**.

---

### 4.4 Balanced Tree

* Height difference between left and right subtrees is minimal
* Example: **AVL Tree**, **Red-Black Tree**

---

### 4.5 Heap

A **complete binary tree** with heap property:

* **Max Heap**: Parent ≥ children
* **Min Heap**: Parent ≤ children

Used in **priority queues**.

---

### 4.6 Trie (Prefix Tree)

* Used for storing strings
* Each node represents a character
* Efficient for prefix-based searching

Applications:

* Autocomplete
* Spell checker

---

## 5. Tree Traversals

Traversal means visiting all nodes of a tree.

### 5.1 Depth First Search (DFS)

#### 1. Inorder (Left → Root → Right)

```text
Used in BST to get sorted data
```

#### 2. Preorder (Root → Left → Right)

```text
Used to copy tree / prefix expression
```

#### 3. Postorder (Left → Right → Root)

```text
Used to delete tree / postfix expression
```

---

### 5.2 Breadth First Search (BFS)

#### Level Order Traversal

* Visits nodes level by level
* Uses **Queue**

---

## 6. Tree Representation

### 6.1 Node-based Representation

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

### 6.2 Array Representation

* Used in heaps
* For index `i`:

  * Left child = `2i + 1`
  * Right child = `2i + 2`

---

## 7. Common Tree Operations

* Insertion
* Deletion
* Searching
* Traversal
* Height calculation
* Counting nodes / leaves

---

## 8. Time Complexity (Binary Tree)

| Operation | Time Complexity |
| --------- | --------------- |
| Search    | O(n)            |
| Insert    | O(n)            |
| Delete    | O(n)            |
| Traversal | O(n)            |

### Binary Search Tree (Average)

* Search / Insert / Delete → **O(log n)**

---

## 9. Applications of Trees

* File systems
* Database indexing (B-Trees)
* Expression evaluation
* Routing algorithms
* HTML DOM
* Artificial Intelligence

---

## 10. Key Differences

### Tree vs Graph

| Tree      | Graph               |
| --------- | ------------------- |
| Acyclic   | Can have cycles     |
| N−1 edges | Any number of edges |
| One root  | No root required    |

---

## 11. Interview Tips 💡

* Always clarify **type of tree**
* Use **recursion** for DFS
* Use **queue** for level order
* Draw tree before coding

---

## 12. Summary

* Trees represent hierarchical data
* Binary trees are the most important
* Traversals are fundamental
* BST and Heap are commonly asked

---

✨ *Trees are the backbone of many advanced data structures. Master them well!*
