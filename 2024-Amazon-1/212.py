from typing import List


class Trie:
    def __init__(self):
        self.children = {}
        self.end = False
    
    def addWord(self, word):
        nd = self
        for w in word:
            if w not in nd.children:
                nd.children[w] = Trie()
            nd =nd.children[w]
        nd.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.addWord(w)
        tmpRes = []
        visited = set()
        def findWordBacktrack(r, c, wordSoFar, node:Trie):
            nonlocal tmpRes
            if r>=len(board) or c>=len(board[0]) or r<0 or c<0 or (r,c) in visited or board[r][c] not in node.children:
                return
            
            visited.add((r,c))
            curChar = board[r][c]
            if node.children[curChar].end:
                tmpRes.append(wordSoFar + curChar)
            
            findWordBacktrack(r+1, c, wordSoFar+curChar, node.children[curChar])
            findWordBacktrack(r-1, c, wordSoFar+curChar, node.children[curChar])
            findWordBacktrack(r, c+1, wordSoFar+curChar, node.children[curChar])
            findWordBacktrack(r, c-1, wordSoFar+curChar, node.children[curChar])
            visited.remove((r,c))
        
        
        all_words = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                ch = board[r][c]
                if ch in trie.children: # possible start of a word
                    tmpRes.clear()
                    findWordBacktrack(r, c, '', trie)
                    all_words.extend(tmpRes)
        return list(set(all_words))
    
s = Solution()

print(s.findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]))

print(s.findWords( board = [["a","b"]], words = ["ba"]))
print(s.findWords([["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]],["oa","oaa"]))