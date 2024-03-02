from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        ## Find the inversion point --> -ve to +ve
        inv = 0
        if nums[inv]<=0:
            while inv<len(nums) and nums[inv]<0:
                inv+=1
        
        #1 inversion location --> in the middle: array has both +ve and -ve numbers
        #2 					 --> in 0th position: array only has +ve
        #3                    --> in the len(num)th position: array only has -ve
        
        result = []
        if inv == 0: #2
            for p in nums:
                result.append(p*p)
        elif inv == len(nums): #3
            for i in range(len(nums)-1, -1, -1):
                result.append(nums[i]*nums[i])
            
        else:
            p1 = inv
            p2 = inv-1
            
            while p2>=0 and p1<len(nums):
                if nums[p1] <= -nums[p2]:
                    result.append(nums[p1]*nums[p1])
                    p1+=1
                else:
                    result.append(nums[p2]*nums[p2])
                    p2-=1
            
            while p2>=0:
                result.append(nums[p2]*nums[p2])
                p2-=1
            while p1<len(nums):
                result.append(nums[p1]*nums[p1])
                p1+=1
        
        return result