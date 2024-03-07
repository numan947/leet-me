# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def findMaxDepth(curNode):
            if curNode == None:
                return 0
            return 1+ max(findMaxDepth(curNode.left), findMaxDepth(curNode.right))
        return findMaxDepth(root)