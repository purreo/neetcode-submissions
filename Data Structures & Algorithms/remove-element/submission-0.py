class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i],nums[k] = nums[k],nums[i]
                k += 1
        return k
            

    # nums = [2,2,3,3], val = 3
 #                k
 #                    i
            
            
                
            