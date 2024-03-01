
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        
        def dfs(node:Node):
            if not node:
                return None
            
            if node in oldToNew:
                return oldToNew[node]
            
            copy:Node = Node(node.val)
            oldToNew[node] = copy
            
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
        
        return dfs(node)