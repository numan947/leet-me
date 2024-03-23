class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.trieRoot = TrieNode()
        

    def addWord(self, word: str) -> None:
        curNode = self.trieRoot
        for c in word:
            if c not in curNode.children:
                curNode.children[c] = TrieNode()
            curNode = curNode.children[c]
        curNode.endOfWord = True

    
    
    def search(self, word: str) -> bool:
        
        def recMatch(node:TrieNode, idx):
            if idx>=len(word): # this should never happen
                return False
            
            c = word[idx]            
            if idx == len(word)-1:
                if c == '.':
                    for ch in node.children:
                        if node.children[ch].endOfWord:
                            return True
                    return False
                if c not in node.children or not node.children[c].endOfWord:
                    return False
                return True
            
            if c == '.':
                matched = False
                for ch in node.children:
                    matched = matched or recMatch(node.children[ch], idx+1)
                return matched
            elif c in node.children:
                return recMatch(node.children[c], idx+1)
            return False
        
        return recMatch(self.trieRoot, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)