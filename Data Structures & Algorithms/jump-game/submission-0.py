# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         n = len(nums)

#         reachable = [False] * n
#         reachable[0] = True

#         for i in range(n):
#             if not reachable[i]:
#                 break
                
#             destination = min(n-1, i + nums[i])
#             if destination == n-1:
#                 break
                
#             for j in range(i, destination + 1):
#                 reachable[j] = True

#         return reachable[n-1]

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        fim = len(nums)-1
        alcancavel = 0
        for i in range(len(nums)):
            if i<=alcancavel:
                alcancavel = max(alcancavel,i+nums[i])
            if alcancavel >= fim:
                return True

        return False