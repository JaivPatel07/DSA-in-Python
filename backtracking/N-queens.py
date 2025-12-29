# ============================================================
# N-QUEEN PROBLEM – BEGINNER FRIENDLY NOTES
# ============================================================

# WHAT IS N-QUEEN?
# Place N queens on N×N chessboard
# No two queens should attack each other

# HOW QUEEN ATTACKS:
# - Same row
# - Same column
# - Same diagonal

# KEY SIMPLIFICATION:
# Place ONE queen per row
# (no need to check same row again)

# TECHNIQUE USED:
# Backtracking (Try → Undo → Try next)

# ------------------------------------------------------------
# IMPORTANT CHECKS
# ------------------------------------------------------------

# Column check:
# col

# Main diagonal:
# row - col

# Anti diagonal:
# row + col

# Use SETS for fast checking (O(1))


# ------------------------------------------------------------
# STEPS (VERY IMPORTANT)
# ------------------------------------------------------------

# 1. Start from row 0
# 2. Try placing queen in each column
# 3. If position is safe → place queen
# 4. Move to next row
# 5. If stuck → remove queen (backtrack)
# 6. If all rows filled → one solution found


# ------------------------------------------------------------
# N-QUEEN CODE
# ------------------------------------------------------------

def solveNQueens(n):
    board = [["."] * n for _ in range(n)]
    result = []

    cols = set()     # stores used columns
    diag1 = set()    # row - col
    diag2 = set()    # row + col

    def backtrack(row):
        # base case: all rows filled
        if row == n:
            result.append(["".join(r) for r in board])
            return

        for col in range(n):
            # check if safe
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue

            # choose (place queen)
            board[row][col] = "Q"
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            # explore next row
            backtrack(row + 1)

            # undo (remove queen)
            board[row][col] = "."
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return result


# ------------------------------------------------------------
# DRIVER CODE
# ------------------------------------------------------------

n = 4
solutions = solveNQueens(n)

for sol in solutions:
    for row in sol:
        print(row)
    print()

# OUTPUT (one solution):
# .Q..
# ...Q
# Q...
# ..Q.
