from math import sqrt


class Solution:
    def primePalindrome(self, n: int) -> int:
        if n<=2:
            return 2
        elif n == 3:
            return 3
        elif n<=5:
            return 5
        elif n<=7:
            return 7
        
        def isPrime(n):
            if n == 0 or n == 1:
                return False
            if n == 2 or n == 3 or n == 5 or n == 7:
                return True
            if n%2 == 0:
                return False
            for i in range(3, int(sqrt(n))+1, 2):
                if n%i == 0:
                    return False
            return True
        
        def isPalinDrome(n):
            t = str(n)
            return t == t[::-1]
        
        if n%2 == 0 and n!=2:
            n+=1
        while True:
            if isPalinDrome(n) and isPrime(n):
                return n
            n+=2
            if 10**7 < n < 10**8:
                n = 10**8
                n+=1

        
s = Solution()

print(s.primePalindrome(3))
print(s.primePalindrome(1))
print(s.primePalindrome(51633903))