class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        s = 0
        e = rows * cols - 1

        while s <= e:
            m = (s + e) // 1

            i = m // cols
            j = m % cols
            curr = matrix[i][j]

            if curr == target:
                return True
            elif curr > target:
                e = m - 1
            else: # curr < target
                s = m + 1
            
        return False
            

        