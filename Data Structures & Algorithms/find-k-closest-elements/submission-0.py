class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        # heap? -> "k" mention
        # sliding window

        # I: sorted array of ints 
        # O: list of k ints closest to x
        # E: k can be in the array
        # C: 1 <= k <= arr.length <= 10,000, -10,000 <= arr[i], x <= 10,000, arr is sorted in ascending order

        l,r = 0,len(nums)-1
        closest = float('inf')
        while r - l + 1 > k:
        # keep shrinking until pointers are of length k
            if (abs(nums[l] - x) > abs(nums[r] - x)):
                l += 1
            else:
               r -= 1
        return nums[l:r+1]
        


            



