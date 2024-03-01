class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        res = 0
        
        def checkithbit(n, i):
            return n & (1<<i)
        
        for t in range(32):
            cnt = 0
            for p in nums:
                if checkithbit(p, t):
                    cnt+=1
            
            if cnt >=k:
                res |= (1<<t)
        
        return res