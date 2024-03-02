from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lft, rgt = 0, len(nums)-1
        
        
        while lft<=rgt:
            mid = lft + (rgt-lft)//2
            
            if nums[mid] == target:
                return mid
            
            # Case -- lft...mid is sorted
            
            if nums[lft]<=nums[mid]:
                # subcase -- target is between nums[lft]...nums[mid]
                if target>=nums[lft] and target<=nums[mid]:
                    ## search left of mid
                    rgt = mid-1
                # subcase -- target is not between nums[lft]..nums[mid]
                else:
                    lft = mid+1
            
            # Case -- mid...rgt is sorted
            else:
                # subcase -- target is between nums[mid]...nums[rgt]
                if target>=nums[mid] and target<=nums[rgt]:
                    lft = mid+1
                # subcase -- target is not between nums[mid]..nums[rgt]
                else:
                    rgt = mid-1
        
        return -1
            
            
            
            


s = Solution()

print(s.search([4,5,6,7,0,1,2], 0))
print(s.search([4,5,6,7,0,1,2], 3))
print(s.search([1], -1))





