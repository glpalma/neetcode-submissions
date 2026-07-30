class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        pivot = self.findMinIndex(nums)
        left = self.binarySearch(nums, 0, pivot-1, target)
        right = self.binarySearch(nums, pivot, n-1, target)

        return left if right == -1 else right

    def binarySearch(self, nums: list[int], start: int, end: int, target: int):
        l = start
        r = end

        while l <= r:
            m = (l+r)//2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            else:
                r = m-1

        return -1


    def findMinIndex(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l+r)//2

            if nums[m-1] >= nums[m]:
                return m
            elif nums[l] <= nums[m] and nums[m] > nums[r]: # [l,m][r]
                # ir pra direita
                l = m+1
            else:
                # elif nums[l] > nums[m] and nums[m] < nums[r]: # [l][m,r]
                # ir pra esquerda
                r = m-1

        return -1

        