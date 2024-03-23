from functools import cache
from typing import List

class Trie:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    def insert(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.endOfWord = True
    
    def lookup(self, word):
        cur = self
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return cur.endOfWord
        
        


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ## this is pure recursive backtracking
        # def dfs(idx):
        #     if idx==len(s):
        #         all_res.append(" ".join(tmpRes))
        #         return True
        #     if idx>len(s):
        #         return False
        #     for w in wordDict:
        #         if len(w) + idx <= len(s) and s[idx:idx+len(w)] == w:
        #             tmpRes.append(w)
        #             dfs(idx+len(w))
        #             tmpRes.pop()
        #     return False
        
        ## Trie + backtracking solution + Memoization
        
        trie = Trie()
        for w in wordDict:
            trie.insert(w)
        
        memo = {}
        
        def dfs(substring):
            if not substring:
                return [[]] # base case            
            
            if substring in memo:
                return memo[substring]
            result = []
            for i in range(len(substring)):
                # print(substring[:i])
                # print(trie.lookup(substring[:i]))
                if trie.lookup(substring[:i+1]): ## prefix length need to be at least 1
                    extensions = dfs(substring[i+1:])
                    for ext in extensions:
                        result.append([substring[:i+1]]+ext) # remembed the dfs is returning list of lists
            memo[substring] = result
            return result
        
        all_res = dfs(s)
        all_res = [" ".join(t) for t in all_res]
        return all_res
    
s = Solution()

print(s.wordBreak( s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]))

# print(s.wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]))