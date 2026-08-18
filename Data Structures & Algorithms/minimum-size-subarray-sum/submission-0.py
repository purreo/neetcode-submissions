class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # I: list of nums
        # O: minimal length of subarray whos sum >= target. 0 if no sub.
        # E: sum will always be positive, nums/target positive
        # C: 1 <= nums[i] <= 10,000, 1 <= target <= 1,000,000,000, 1 <= nums.length <= 100,000

        # variable sliding window to find subarray sums
        l = 0
        min_len = float('inf')
        sum = 0
        for r,num in enumerate(nums):
            sum += num
            while sum >= target:
                sum -= nums[l]
                min_len = min(min_len,r-l+1)
                l += 1
        return min_len if min_len != float('inf') else 0

            
            

