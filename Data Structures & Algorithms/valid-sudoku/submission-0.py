class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        n = 9
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        squares = [set() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                k = board[i][j]
                if k == ".":
                    continue
                
                sq = int((i // 3) * 3 + (j // 3))

                if k in rows[i] or k in cols[j] or k in squares[sq]:
                    return False

                rows[i].add(k)
                cols[j].add(k)
                squares[sq].add(k)
        
        return True
