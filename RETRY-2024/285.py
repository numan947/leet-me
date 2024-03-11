class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root:TreeNode, p:TreeNode):
        # write your code here
        if not root:
            return root
        succ = None
        while root != p:
            if p.val<=root.val:
                succ = root
                root = root.left
            else:
                root = root.right
        
        # we found p here, so we need to potentially update the succ
        
        if p.right:
            root = p.right
            while root:
                succ = root
                root = root.left
        
        return succ