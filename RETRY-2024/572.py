# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(tree1:TreeNode, tree2:TreeNode):
            if tree1 == None and tree2 == None:
                return True
            if not tree1 or not tree2:
                return False
            
            if tree1.val != tree2.val:
                return False
            
            return isSameTree(tree1.left, tree2.left) and isSameTree(tree1.right, tree2.right)
        
        
        def subTreeCheck(node, subTreeRoot):
            if node == None and subTreeRoot == None:
                return True
            if not node or not subTreeRoot:
                return False
            
            if node.val == subTreeRoot.val:
                if isSameTree(node, subTreeRoot):
                    return True
            if subTreeCheck(node.left, subTreeRoot):
                return True
            return subTreeCheck(node.right, subTreeRoot)
        
        return subTreeCheck(root, subRoot)