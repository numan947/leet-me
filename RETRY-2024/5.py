from functools import cache


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # ## two pointers
        # maxLen = 0
        # ans = ""
        # for i in range(len(s)):
        #     p1 = i
        #     p2 = i
        #     while p1>=0 and p2<len(s) and s[p1] == s[p2]:
        #         if p2-p1+1 > maxLen:
        #             maxLen = p2-p1+1
        #             ans = s[p1:p2+1] 
        #         p1-=1
        #         p2+=1
            
        #     p1 = i
        #     p2 = i+1        
        #     while p1>=0 and p2<len(s) and s[p1] == s[p2]:
        #         if p2-p1+1 > maxLen:
        #             maxLen = p2-p1+1
        #             ans = s[p1:p2+1] 
        #         p1-=1
        #         p2+=1
        # return ans
        
        n = len(s)
        if not n:
            return ""
        
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        ansStart, ansEnd = 0, 0
        
        for end in range(0, n):
            for start in range(end-1, -1, -1):
                if s[start] == s[end]:
                    if end-start == 1 or  dp[start+1][end-1]:
                        dp[start][end] = True
                        if (ansEnd-ansStart+1)<(end-start+1):
                            ansStart = start
                            ansEnd = end
        return s[ansStart:ansEnd+1]

s = Solution()
print(s.longestPalindrome("aacabdkacaa"))