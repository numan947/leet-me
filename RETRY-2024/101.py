# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def checkSym(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.checkSym(left.left, right.right) and self.checkSym(left.right, right.left)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left  and not root.right):
            return True
        if (not root.left or not root.right):
            return False
        return self.checkSym(root.left, root.right)
        