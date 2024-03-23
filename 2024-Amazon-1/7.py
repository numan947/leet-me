from math import fmod


class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31 - 1
        MIN = -2**31
        mult = 1 if x>0 else -1
        x = abs(x)
        tmp = 0
        while x>0:
            if mult:
                if tmp>MAX//10: # this should overflow
                    return 0
                elif tmp == MAX//10 and x%10>MAX%10:
                    return 0 # another overflow
            else:
                if -tmp < MIN//10:
                    return 0
                elif -tmp == MIN//10 and x%10 > fmod(MIN, 10):
                    return 0             
            tmp*=10
            tmp+=(x%10)
            x//=10
        return mult*tmp

s = Solution()
# print(s.reverse(-123))
print(s.reverse(-1534236469))