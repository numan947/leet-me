class Solution:
    def longestPalindrome(self, s: str) -> str:
        # two ways == iterative and span from middle
        maxLen = 0
        ans = (-1, -1)
        for i in range(len(s)):
            l = r = i            
            while l>=0 and r<len(s) and s[l] == s[r]:
                if maxLen < (r-l+1):
                    maxLen = r-l + 1
                    ans = (l , r+1)
                l-=1
                r+=1
            l = r = i
            r+=1            
            while l>=0 and r<len(s) and s[l] == s[r]:
                if maxLen < (r-l+1):
                    maxLen = r-l + 1
                    ans = (l , r+1)
                l-=1
                r+=1
        return s[ans[0]:ans[1]]