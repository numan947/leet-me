class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r = -1, len(nums)
        c = 0 
        
        while c < r:
            if nums[c] == 0:
                l += 1
                nums[l], nums[c] = nums[c], nums[l]
                c+=1
                
            elif nums[c] == 2:
                r-=1
                nums[c], nums[r] = nums[r], nums[c]
            else:
                c+=1