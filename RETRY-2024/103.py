# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        
        q.append(root)
        level = 0
        result = []
        while q:
            tmpRes = []
            for _ in range(len(q)):
                cur = q.popleft()
                tmpRes.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            
            if level%2:
                tmpRes.reverse()
            result.append(tmpRes)
            level+=1
        
        return result