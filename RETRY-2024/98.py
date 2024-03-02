# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def checkValid(self, root:TreeNode, left:TreeNode, right:TreeNode):
        if root == None:
            return True
        if left.val < root.val and root.val < right.val:
            return self.checkValid(root.left, left, root) and self.checkValid(root.right, root, right)
        return False
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.checkValid(root, TreeNode(float('-inf')), TreeNode(float('inf')))