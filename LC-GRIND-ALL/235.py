# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def findLCA(cur):
            if cur == None:
                return None
            
            if p.val < cur.val and q.val < cur.val:
                return findLCA(cur.left)
            elif p.val>cur.val and q.val>cur.val:
                return findLCA(cur.right)
            return cur
        
        return findLCA(root)