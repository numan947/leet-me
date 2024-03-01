# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def checkBalance(node):
            if node is None:
                return (0, True) # (height, isBalanced)
            
            lh, lb = checkBalance(node.left)
            rh, rb = checkBalance(node.right)
            
            if lb and rb:
                return (1+max(lh, rh), abs(lh-rh)<=1)
            return (1+max(lh, rh), False)
        
        h,b = checkBalance(root)
        return b