# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adjList = {}
        
        def makeGraph(node:TreeNode):
            if not node:
                return
            
            if node not in adjList:
                adjList[node] = []
            
            if node.right:
                adjList[node].append(node.right)
                if node.right not in adjList:
                    adjList[node.right] = []
                adjList[node.right].append(node)
                makeGraph(node.right)
            
            if node.left:
                adjList[node].append(node.left)
                if node.left not in adjList:
                    adjList[node.left] = []
                adjList[node.left].append(node)
                makeGraph(node.left)
        
        makeGraph(root)
        
        res = []
        dist = {}
        dist[target] = 0
        
        dq = deque()
        
        dq.append(target)
        
        while dq:
            cur = dq.popleft()
            if dist[cur] == k:
                res.append(cur.val)
            else:
                for nxt in adjList[cur]:
                    if nxt not in dist.keys():
                        dist[nxt] = dist[cur] + 1
                        dq.append(nxt)
        
        return res