# Minimax Algorithm
---
The **Minimax Algorithm** is a decision-making algorithm used in **two-player games** where:
* One player wants to **win**
* The other player wants to **stop them from winning**
The algorithm helps a player decide the **best possible move**, assuming the opponent also plays perfectly.

---
Minimax works best when the game has:

* Two players
* Turn-based moves
* No hidden information
* One winner and one loser (zero-sum)

Examples:

* Tic Tac Toe
* Chess
* Checkers
* Connect Four
---

## MAX and MIN Players
### MAX Player

* Tries to **maximize** the score
* Wants the best outcome
* Usually the AI or computer

### MIN Player

* Tries to **minimize** the score
* Wants the worst outcome for MAX
* Usually the human

---

## 5️⃣ What is a Game Tree?

A **game tree** is a diagram that shows:

* All possible moves
* All possible future game states

Each level represents a player's turn.

Example:

```
        MAX
       /   \
     MIN   MIN
    /   \   /  \
   1    -1  0   1
```

Each path represents a possible future.

---

## 6️⃣ Terminal States and Scores

A **terminal state** is when the game ends.

We assign scores:

* **+1** → MAX wins
* **-1** → MIN wins
* **0** → Draw

These scores help the algorithm decide.

---

## 7️⃣ Step-by-Step Working of Minimax

1. Start from the current game state
2. Generate all possible moves
3. Go deeper until the game ends
4. Assign scores at the bottom
5. Go back up the tree
6. MAX chooses the highest value
7. MIN chooses the lowest value

This process is called **backtracking**.

---

## 8️⃣ Simple Example (Tic Tac Toe)

Imagine the board is almost full.

Minimax:

* Tries every empty cell
* Simulates both players
* Calculates win, lose, or draw
* Picks the safest move

Result: The AI never loses.

---

## 9️⃣ Minimax Pseudocode Explained

```text
function minimax(state, isMax):
    if game over:
        return score

    if isMax:
        return maximum value of all moves
    else:
        return minimum value of all moves
```

### Plain English Explanation:

* If game ends → return result
* If it is MAX's turn → pick best score
* If it is MIN's turn → pick worst score

---

## 🔟 Python Implementation (Beginner Friendly)

```python
def minimax(board, is_max):
    if winner(board, 'X'):
        return 1
    if winner(board, 'O'):
        return -1
    if draw(board):
        return 0

    if is_max:
        best = -1000
        for move in moves(board):
            board[move] = 'X'
            best = max(best, minimax(board, False))
            board[move] = ' '
        return best
    else:
        best = 1000
        for move in moves(board):
            board[move] = 'O'
            best = min(best, minimax(board, True))
            board[move] = ' '
        return best
```

Do not worry if you don’t fully understand this now — understanding the **idea** is more important.

---

## 1️⃣1️⃣ Alpha-Beta Pruning (Optimization)

Minimax can be slow.

**Alpha-Beta Pruning** helps by:

* Skipping unnecessary branches
* Reducing calculations

### Alpha (α)

Best score MAX can guarantee

### Beta (β)

Best score MIN can guarantee

If Alpha ≥ Beta → stop exploring

---

## 1️⃣2️⃣ Time and Space Complexity

| Type  | Complexity |
| ----- | ---------- |
| Time  | O(b^d)     |
| Space | O(d)       |

Where:

* `b` = number of possible moves
* `d` = depth of game tree

---

## 1️⃣3️⃣ Advantages and Limitations

### ✅ Advantages

* Always finds optimal move
* Perfect for small games
* Easy to understand conceptually

### ❌ Limitations

* Slow for large games
* High computation cost

---

## 1️⃣4️⃣ Real-World Applications

* Game AI
* Strategy planning
* Decision-making systems
* AI learning foundations

---

## 1️⃣5️⃣ Summary

* Minimax is a smart decision algorithm
* Used in two-player games
* Assumes optimal opponent
* Foundation of game AI

If you understand Minimax, you understand **how machines think ahead** 🧠

---

✨ *Happy Learning!* ✨
