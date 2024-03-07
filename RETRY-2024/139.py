from functools import cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        def match(idx, t):
            for p in range(len(t)):
                if idx == len(s):
                    return False
                if s[idx] != t[p]:
                    return False
                idx+=1
            return True
        
        memo = {}
        def possible(idx):
            if idx in memo.keys():
                return memo[idx]
            if idx>len(s):
                return False
            if idx == len(s):
                return True
            for t in wordDict:
                if match(idx, t) and possible(idx+len(t)):
                    memo[idx] = True
                    return True
            return False
        
        return possible(0)