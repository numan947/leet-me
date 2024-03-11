from typing import List

class TrieNode:
    def __init__(self):
        self.name = None
        self.is_file = False
        self.content = []
        self.children = {}
        
    def insert(self, path:str, is_file:bool = False)->'TrieNode':
        node = self
        parts = path.split('/')
        
        for part in parts[1:]:
            if part not in node.children:
                node.children[part] = TrieNode()
            node = node.children[part]
        
        node.is_file = is_file
        
        if is_file:
            node.name = parts[-1]
        
        return node
    
    def search(self, path:str, is_file:bool=False)->'TrieNode':
        node = self
        parts = path.split('/')
        for p in parts[1:]:
            if p not in node.children:
                return None
            node = node.children[p]
        
        if node.is_file == is_file:
            return node
        return None

class FileSystem:
    def __init__(self):
        self.root = TrieNode()
    
    def ls(self, path:str)->List[str]:
        node:TrieNode = self.root.search(path)
        if not node:
            return []
        if node.is_file:
            return [node.name]
        return sorted(node.children.keys())
        
    def mkdir(self, path:str) -> None:
        self.root.insert(path)
    
    def addContentToFile(self, filePath:str, content:str) -> None:
        node:TrieNode = self.root.insert(filePath, is_file=True)
        node.content.append(content)
    
    def readContentFromFile(self, filePath:str)->str:
        node:TrieNode = self.root.search(filePath, is_file=True)
        if not node:
            raise FileNotFoundError(f"File Not Found at {filePath}")
        return ''.join(node.content)


fs = FileSystem()

print(fs.mkdir("/a/b/c"))
print(fs.addContentToFile("/a/b/c/x", "Hello World!"))
print(fs.ls("/a/b/c"))
print(fs.readContentFromFile("/a/b/c/x"))