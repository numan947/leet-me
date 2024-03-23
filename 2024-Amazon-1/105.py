# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        cur = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        preorder.pop(0)
        cur.left = self.buildTree(preorder, inorder[:idx])
        cur.right = self.buildTree(preorder, inorder[idx+1:])
        return cur
        