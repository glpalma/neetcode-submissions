from math import ceil

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        lower = 1
        upper = max(piles)

        best = upper
        while lower <= upper:
            k = (lower + upper) // 2

            t = 0
            for p in piles: # how much time it takes to consume all piles with current k
                t += ceil(p/k)
            
            # t ruim eu alivio aumentando o lower
            # t bom eu restrinjo baixando o upper
            # vai indo até convergir

            if t > h:
                lower = k + 1
            else: # t <= h
                upper = k - 1
                best = min(best, k)

        return best