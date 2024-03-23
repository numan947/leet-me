# Definition for a binary tree node.
from sympy import flatten


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root:TreeNode):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        ## Pre-order traversal
        flattened = []
        def dfs(node:TreeNode):
            if not node:
                flattened.append("NULL")
                return
            flattened.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return "#".join(flattened)

    def deserialize(self, data:TreeNode):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        flattened = data.split("#")
        CUR_NODE = 0
        
        def dfs():
            nonlocal CUR_NODE
            if flattened[CUR_NODE] == "NULL":
                CUR_NODE+=1
                return None
            node = TreeNode(int(flattened[CUR_NODE]))
            CUR_NODE+=1
            node.left = dfs()
            node.right = dfs()
            
            return node
        
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))