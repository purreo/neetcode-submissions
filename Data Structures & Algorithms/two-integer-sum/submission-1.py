class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compMap = {}
        for i,num in enumerate(nums):
            if target - num in compMap:
                return [compMap[target - num],i]
            compMap[num] = i
        return -1