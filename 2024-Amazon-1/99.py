from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        # find the two inversionset
        invSet1 = None
        invSet2 = None
        prev = None
        
        def bstTrav(root:TreeNode):
            nonlocal prev, invSet1, invSet2
            if not root:
                return
            bstTrav(root.left)
            
            if prev and prev.val>root.val:
                if not invSet1:
                    invSet1 = (prev, root)
                else:
                    invSet2 = (prev, root)
            prev = root
            bstTrav(root.right)
            
        bstTrav(root)
        
        if invSet1 and invSet2:
            invSet1[0].val, invSet2[1].val = invSet2[1].val, invSet1[0].val
        elif invSet1:
            invSet1[0].val, invSet1[1].val = invSet1[1].val, invSet1[0].val  
        