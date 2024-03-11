class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x<0:
            return False
        
        def reverseNum(n):
            rev = 0
            while n:
                rev*=10
                rev+=n%10
                n=n//10
            return rev
        
        return x == reverseNum(x)
        
        