# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root:TreeNode):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        trav = []
        def dfs(rt:TreeNode):
            if rt == None:
                trav.append("NULL")
                return
            trav.append(str(rt.val))
            dfs(rt.left)
            dfs(rt.right)
            return
        
        dfs(root)
        
        return ','.join(trav)
            
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        trav = data.split(',')
        self.cur = 0
        
        def dfs():
            if self.cur >= len(trav):
                return
            if trav[self.cur] == "NULL":
                self.cur+=1
                return None
            rt = TreeNode(int(trav[self.cur]))
            self.cur += 1
            rt.left = dfs()
            rt.right = dfs()
            return rt 
            
        return dfs()
        # return root
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))