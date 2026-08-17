class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L, R = 0, len(nums)-1
        while L < R:
            sum = nums[L] + nums[R]
            if sum == target:
                return [L+1,R+1]
            elif sum > target:
                R -= 1
            else:
                L += 1
        return []