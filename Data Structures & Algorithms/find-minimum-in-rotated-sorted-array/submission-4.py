class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l+r)//2

            #ou lm/r ou l/mr

            if nums[m-1] >= nums[m]:
                return nums[m]
            elif nums[l] <= nums[m] and nums[m] > nums[r]: # [l,m][r]
                # ir pra direita
                l = m+1
            else:
                # elif nums[l] > nums[m] and nums[m] < nums[r]: # [l][m,r]
                # ir pra esquerda
                r = m-1

        return -1
