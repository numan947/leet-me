from functools import cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # @cache
        # def dfs(pos):
        #     if pos == len(s):
        #         return True
        #     if pos>len(s):
        #         return False
        #     for w in wordDict:
        #         if pos+len(w)<=len(s) and s[pos:pos+len(w)] == w:
        #             if dfs(pos + len(w)):
        #                 return True
        #     return False
        # return dfs(0)
        
        dp = [False]*(len(s)+1) ## last position is base case, so it needs to be set true
        dp[len(s)] = True
        
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i+len(w)<=len(s) and s[i:i+len(w)] == w):
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]
        
s = Solution()

print(s.wordBreak(s = "leetcode", wordDict = ["leet","code"]))
print(s.wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))
print(s.wordBreak(s = "applepenapple", wordDict = ["apple","pen"]))