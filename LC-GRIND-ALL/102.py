# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq = deque()
        ans = []
        if not root:
            return ans
        
        dq.append(root)
        
        while dq:
            ls = len(dq)
            le = []
            while ls:
                t = dq.popleft()
                if t is None:
                    continue
                le.append(t.val)
                
                if t.left:
                    dq.append(t.left)
                if t.right:
                    dq.append(t.right)
                ls-=1
            ans.append(le)
        
        return ans