from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.taken = set()
        res = []
        tmp = []
        def findPermutation():
            if len(self.taken) == len(nums):
                res.append(list(tmp))
                return
            
            for n in nums:
                if n not in self.taken:
                    self.taken.add(n)
                    tmp.append(n)
                    findPermutation()
                    tmp.pop()
                    self.taken.remove(n)
        
        findPermutation()
        
        return res 