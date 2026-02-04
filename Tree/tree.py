# ============================================================
# TREE – PRACTICE QUESTIONS WITH ANSWERS
# ============================================================

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ------------------------------------------------------------
# Q1. MAXIMUM DEPTH OF BINARY TREE
# ------------------------------------------------------------
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

# ------------------------------------------------------------
# Q2. INVERT BINARY TREE
# ------------------------------------------------------------
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

def invertTree(root):
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root

# ------------------------------------------------------------
# Q3. SAME TREE
# ------------------------------------------------------------
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

# ------------------------------------------------------------
# Q4. BINARY TREE LEVEL ORDER TRAVERSAL (BFS)
# ------------------------------------------------------------
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

def levelOrder(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

if __name__ == "__main__":
    # Test Case:
    #      3
    #     / \
    #    9  20
    #      /  \
    #     15   7
    
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(f"Max Depth: {maxDepth(root)}")
    print(f"Level Order: {levelOrder(root)}")