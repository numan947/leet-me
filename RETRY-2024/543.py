# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node:Optional[TreeNode]) ->  tuple[int, int]: # maxDiameter, maxDepth
            if node == None:
                return (0,0)
            
            mxDiamLeft, maxDepthLeft = dfs(node.left)
            mxDiamRight, maxDepthRight = dfs(node.right)
            
            retDepth = max(maxDepthLeft, maxDepthRight) + 1
            retDiam = max(maxDepthLeft + maxDepthRight , mxDiamLeft,mxDiamRight)
            
            return (retDiam, retDepth)
        
        
        return dfs(root)[0]