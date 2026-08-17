class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        while l < r:
            m = (r+l)//2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        if l < len(nums) and l > -1 and nums[l] == target:
            return l
        else:
            return -1