class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        num = 0
        num_started = False
        for c in s:
            if c == ' ' and not num_started:
                continue
            elif c == '+' and not num_started:
                sign = 1
                num_started = True
            elif c == '-' and not num_started:
                sign = -1
                num_started = True
            elif ord(c)>=ord('0') and ord(c)<=ord('9'):
                num = num*10 + (ord(c) - ord('0'))
                num_started = True
            else:
                break
        res = num*sign
        
        if res<-2147483648:
            return -2147483648
        elif res > 2147483647:
            return 2147483647
        return res