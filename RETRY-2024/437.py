# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        seenBefore = {0:1}
        
        def countPaths(node:TreeNode, totalSum):
            if not node:
                return 0
            
            totalSum += node.val
            
            pathCounts = 0
            if (totalSum-targetSum) in seenBefore:
                pathCounts += seenBefore[totalSum-targetSum]
            seenBefore[totalSum] = seenBefore.get(totalSum, 0)+1
            pathCounts += countPaths(node.left, totalSum)
            pathCounts += countPaths(node.right, totalSum)
            seenBefore[totalSum] = seenBefore.get(totalSum, 0)-1
            
            return pathCounts
        
        return countPaths(root, 0)
            