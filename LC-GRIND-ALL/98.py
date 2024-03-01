# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def makeValid(node, left, right):
            if node == None:
                return True
            if left >= node.val or right<=node.val:
                return False
            
            return makeValid(node.left, left, node.val) and makeValid(node.right, node.val, right)

        return makeValid(root, float('-inf'), float('inf'))