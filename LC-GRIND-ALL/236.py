# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def findLCA(node, p, q): # returns (foundP:bool, foundQ:bool, ans)
            if node == None:
                return (False, False, None)
            
            lp, lq, la = findLCA(node.left, p, q)
            rp, rq, ra = findLCA(node.right, p, q)
            
            if la:
                return (lp, lq, la)
            elif ra:
                return (rp, rq, ra)
            else:
                if (lp or rp) and (lq or rq):
                    return (True, True, node)
                if node.val == p.val:
                    if lq or rq:
                        return (True, True, node)
                    else:
                        return (True, False, None)
                elif node.val == q.val:
                    if lp or rp:
                        return (True, True, node)
                    else:
                        return (False, True, None)
                else:
                    if lp or rp:
                        return (True, False, None)
                    elif lq or rq:
                        return (False, True, None)
                    return (False, False, None)
        
        _,_,ans = findLCA(root, p, q)
        return ans