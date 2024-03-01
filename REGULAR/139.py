from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def match(idx, t):
            for p in range(len(t)):
                if idx == len(s):
                    return False
                if s[idx] != t[p]:
                    return False
                idx+=1
            return True

        @cache
        def solve(idx): # curIdx for the word
            # print(idx)
            if idx == len(s):
                return True
            possible = False
            for t in wordDict:
                if match(idx, t) and (solve(idx+len(t))):
                    possible = True
                    break
            return possible
        
        return solve(0)

s = Solution()

print(s.wordBreak("leetcode", ["leet","code"]))