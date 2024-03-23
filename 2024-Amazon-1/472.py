from typing import List

from numpy import tri

class Trie:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def add(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.endOfWord = True
    
    def search(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord
        
        
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        ## Backtracking + Trie
        # words.sort(key=lambda x: len(x))
        # result = []
        # trie = Trie()
        
        # def dfs(substring):
        #     if not substring:
        #         return True
        #     node:Trie = trie
        #     for i, c in enumerate(substring):
        #         if c not in node.children:
        #             return False
        #         node = node.children[c]
                
        #         if node.endOfWord and dfs(substring[i+1:]):
        #             return True
        #     return False
        
        # for ww in words:
        #     if dfs(ww):
        #         result.append(ww)
        #     else:
        #         trie.add(ww)
        # return result
        hashSet = set(words)
        memo = {}
        def dfs(word):
            if not word:
                return True
            if word in memo:
                return memo[word]
            success = False
            for i in range(1, len(word)): # splitting into prefix:suffix, where len(prefix)>=1 and len(suffix)>=1
                pref = word[:i]
                suff = word[i:]
                if (pref in hashSet and suff in hashSet) or (pref in hashSet and dfs(suff)):
                    success = True
                    break
            memo[word] = success
            return success
        
        res = []
        for w in words:
            if dfs(w):
                res.append(w)
        return res
