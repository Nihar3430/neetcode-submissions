from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashrow = defaultdict(set)
        hashcol = defaultdict(set)
        hashbox = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in hashrow[r] or board[r][c] in hashcol[c] or board[r][c] in hashbox[(r//3,c//3)]:
                    return False
                else:
                    hashrow[r].add(board[r][c])
                    hashcol[c].add(board[r][c])
                    hashbox[(r//3,c//3)].add(board[r][c])

        return True