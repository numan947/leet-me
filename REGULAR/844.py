class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        p1 = len(s) - 1
        p2 = len(t) - 1
        
        while(p1>=0 or p2>=0):
            skipP1 = 0
            while(p1>=0 and (s[p1] == '#' or skipP1)):
                if s[p1] == '#':
                    skipP1+=1
                    p1-=1
                elif skipP1:
                    skipP1-=1
                    p1-=1
            
            skipP2 = 0
            while(p2>=0 and (t[p2] == '#' or skipP2)):
                if t[p2] == '#':
                    skipP2+=1
                    p2-=1
                elif skipP2:
                    p2-=1
                    skipP2-=1
            if (p1>=0 ) != (p2>=0):
                return False
            if (p1<0 and p2<0):
                #both empty strings
                return True
            if p1>=0 and p2>=0:
                if s[p1]!=t[p2]:
                    return False
                p1-=1
                p2-=1
        
        
        if p1 == p2:
            return True
        return False
    
s = Solution()


print(s.backspaceCompare("nzp#o#g","b#nzp#o#g"))

print(s.backspaceCompare("bxj##tw", "bxo#j##tw"))

print(s.backspaceCompare("xywrrmp", "xywrrmu#p"))