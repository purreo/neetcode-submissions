class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = []
        for num in count:
            if count[num] > len(nums) / 2:
               return num
        return -1
        
