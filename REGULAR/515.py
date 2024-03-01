# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import List, Optional
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        dq = deque()
        res = []
        dq.append(root)
        while dq:
            levelSize = len(dq)
            maxVal = float('-inf')
            
            while levelSize:
                cur = dq.popleft()
                maxVal = max(cur.val, maxVal)
                levelSize-=1
                
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
            res.append(int(maxVal))
        
        return res
                