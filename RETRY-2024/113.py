# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        tempArr = []
        
        def findAll(node:TreeNode):
            if node == None: # we have reached a leaf
                if tempArr and sum(tempArr) == targetSum:
                    result.append([x for x in tempArr])
                return
            
            tempArr.append(node.val)
            if not node.left and not node.right:
                if tempArr and sum(tempArr) == targetSum:
                    result.append([x for x in tempArr])
                tempArr.pop()
                return
            if node.left:
                findAll(node.left)
            if node.right:
                findAll(node.right)
            tempArr.pop()
        findAll(root)
        return result