class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        
        while n:
            # res += n%2
            # n = n>>1
            n = (n&(n-1)) # only look at the 1s, do not look at the zeros
            res+=1
        return res