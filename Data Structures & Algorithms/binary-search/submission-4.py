class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1

        while l <= r:
            m = (l+r) // 2
            curr = nums[m]

            if curr == target:
                return m
            elif curr > target:
                r = m - 1
            else: # curr < target
                l = m + 1


        return -1        