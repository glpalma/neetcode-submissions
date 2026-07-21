class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for i, n in enumerate(nums):
            complements[n] = i
        
        for i, n in enumerate(nums):
            if target - n in complements.keys() and i != complements[target-n]:
                return [i, complements[target-n]] 
        
        return [-1,-1]


        