# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = None
        def maxSum(node:Optional[TreeNode]):
            if node == None:
                return 0
            lftMax = maxSum(node.left)
            rgtMax = maxSum(node.right)
            maxPossible = max(lftMax+rgtMax+node.val, lftMax + node.val, rgtMax+node.val, node.val)
            maxPathSum = max(lftMax + node.val, rgtMax+node.val, node.val)
            if self.result is None:
                self.result = maxPossible 
            else:
                self.result = max(self.result, maxPossible)
            return maxPathSum
        
        maxSum(root)
        return self.result