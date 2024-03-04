from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m1, c1 = None, 0
        m2, c2 = None, 0
        
        
        for n in nums:
            if n == m1:
                c1 += 1
            
            elif n == m2:
                c2 += 1
            
            elif c1 == 0:
                m1 = n
                c1 = 1
            elif c2 == 0:
                m2 = n
                c2 = 1
            else:
                c1-=1
                c2-=1
        
        res = []
        cnt = 0
        for t in nums:
            if t == m1:
                cnt+=1
        if cnt>(len(nums)//3):
            res.append(m1)
        cnt = 0
        for t in nums:
            if t == m2:
                cnt+=1
        if cnt>(len(nums)//3):
            res.append(m2)
        
        return res
        