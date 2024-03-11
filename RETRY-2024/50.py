class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        @cache
        def findPow(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            
            tmpRes = self.myPow(x, n//2)
            if n%2:
                return x*tmpRes*tmpRes
            else:
                return tmpRes*tmpRes
        
        tmpN = abs(n)
        
        res = findPow(x, tmpN)
        
        return res if n>=0 else 1/res
        