class Solution:

    def calcPow(self, x, n):
        if n == 1:
            return x
        if n == 0:
            return 1
        if n % 2:
            return x * self.calcPow(x, n-1)
        else:
            tmp = self.calcPow(x, n//2)
            return tmp*tmp

    def myPow(self, x: float, n: int) -> float:
        absn = abs(n)
        ans = self.calcPow(x, absn)
        
        if n < 0:
            return 1.0/ans
        return ans