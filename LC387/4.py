from typing import List
import bisect

class Solution:
    def count_elements_greater_than(self, s, value):
        sorted_s = sorted(s)
        index = bisect.bisect_right(sorted_s, value)
        return len(sorted_s) - index
    
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        
        ops = len(nums)-2
        
        for i in range(2, len(nums)):
            c1 = self.count_elements_greater_than(arr1, nums[i])
            c2 = self.count_elements_greater_than(arr2, nums[i]) 
            if c1>c2:
                arr1.append(nums[i])
            elif c1<c2:
                arr2.append(nums[i])
            else:
                if len(arr1) > len(arr2):
                    arr2.append(nums[i])
                else:
                    arr1.append(nums[i])
        
        arr1.extend(arr2)
        return arr1


s = Solution()
