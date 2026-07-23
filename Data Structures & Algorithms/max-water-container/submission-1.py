class Solution:
    def maxArea(self, heights: list[int]) -> int:
        n = len(heights)

        l = 0
        r = n-1

        maxAmount = 0

        while l < r:
            amount = (r - l) * min(heights[l], heights[r])
            maxAmount = max(amount, maxAmount)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxAmount
        