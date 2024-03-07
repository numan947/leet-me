class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s)<=1:
            return len(s) # intersecting prefix or suffix  
        l,r = 0, len(s)-1
        deleted = 0
        while l<r:
            if s[l] != s[r]:
                break
            else:
                curChar = s[l]             
                while l<=r and s[l] == curChar:
                    l+=1
                    deleted+=1
                
                while l<=r and s[r] == curChar:
                    r-=1
                    deleted+=1
        return len(s) - deleted