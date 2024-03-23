from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []
        self.endOfWord = False
    
    def add(self, word):
        cur:TrieNode = self
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
            if len(cur.suggestions)<3:
                cur.suggestions.append(word)
        cur.endOfWord = True
    
    def search(self, pref, stNode):
        if stNode == None:
            return None
        cur:TrieNode = stNode
        for w in pref:
            if w not in cur.children:
                return None
            cur = cur.children[w]
        return cur
        
        
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
		## Two Pointer Solution
        # res = []
        # products.sort()
        
        # l ,r = 0, len(products)-1
        
        # for i in range(len(searchWord)):
        #     c = searchWord[i]
            
        #     while l<=r and (len(products[l])<=i or products[l][i]!=c):
        #         l+=1
        #     while l<=r and (len(products[r])<=i or products[r][i]!=c):
        #         r-=1
        #     res.append([])
        #     valid_count = r - l + 1
        #     for t in range(min(3, valid_count)):
        #         res[-1].append(products[l+t])
        
        # return res
        
        ## Trie Solution
        
        trie = TrieNode()
        products.sort()
        for p in products:
            trie.add(p)
        
        res = []
        tmp = trie
        for i in range(len(searchWord)):
            tmp:TrieNode = trie.search(searchWord[i], tmp)
            if tmp:
                res.append(tmp.suggestions)
            else:
                res.append([])
        return res

s = Solution()

print(s.suggestedProducts(products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
))