class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        cur = 0
        
        while cur < len(s):
            
            if s[cur] == 'I':
                if cur+1 < len(s):
                    if s[cur+1] == 'V':
                        num+=4
                        cur+=2
                        continue
                    elif s[cur+1] == 'X':
                        num+=9
                        cur+=2
                        continue
                num+=1
                cur+=1
                
            elif s[cur] == 'V':
                cur+=1
                num+=5
            
            elif s[cur] == 'X':
                if cur+1 < len(s):
                    if s[cur+1] == 'L':
                        num+=40
                        cur+=2
                        continue
                    elif s[cur+1] == 'C':
                        num+=90
                        cur+=2
                        continue
                
                cur+=1
                num+=10
            elif s[cur] == 'L':
                num+=50
                cur+=1
            elif s[cur] == 'C':
                if cur+1 < len(s):
                    if s[cur+1] == 'D':
                        num+=400
                        cur+=2
                        continue
                    elif s[cur+1] == 'M':
                        num+=900
                        cur+=2
                        continue
                num+=100
                cur+=1
            
            elif s[cur] == 'D':
                num+=500
                cur+=1
            elif s[cur] == 'M':
                num+=1000
                cur+=1
        
        return num
                
            