# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        idMap = {} # node -> id
        maxWidth = 0
        dq = deque()
        dq.append(root)
        idMap[root] = 1
        
        while dq:
            curLevelSize = len(dq)
            maxWidth = max(maxWidth, 1+abs(idMap[dq[0]] - idMap[dq[-1]]))
            for _ in range(curLevelSize):
                cur = dq.popleft()
                if cur.left:
                    idMap[cur.left] = 2*idMap[cur]+1
                    dq.append(cur.left)
                if cur.right:
                    idMap[cur.right] = 2*idMap[cur]+2
                    dq.append(cur.right) 
        return maxWidth