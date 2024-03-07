class TrieNode:
    def __init__(self, c=None, isEndWord = False):
        self.c = c
        self.isEndWord = isEndWord
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()
        

    def addWord(self, word: str) -> None:
        curNode = self.trie
        for c in word:
            if c not in curNode.children.keys():
                curNode.children[c] = TrieNode(c = c)
            curNode = curNode.children[c]
        curNode.isEndWord = True


    
    def search(self, word: str) -> bool:
        
        def dfs(start, root:TrieNode):
            cur = root

            for i in range(start, len(word)):
                if word[i] == '.':
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if word[i] not in cur.children.keys():
                        return False
                    cur = cur.children[word[i]]
            return cur.isEndWord
        
        return dfs(0, self.trie)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)