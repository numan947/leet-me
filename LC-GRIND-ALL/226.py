# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invertMTree(root):
            if root == None:
                return None
            root.left = invertMTree(root.left)
            root.right = invertMTree(root.right)
            root.left, root.right = root.right,root.left
            return root
        
        return invertMTree(root)
            