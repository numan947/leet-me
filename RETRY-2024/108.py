# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def makeTree(l, r):
            if r<l:
                return None
            if l == r:
                return TreeNode(nums[l])
            
            mid = l+(r-l)//2
            
            # print(l, mid, r)
            
            cur = TreeNode(nums[mid])
            cur.left = makeTree(l, mid-1)
            cur.right = makeTree(mid+1, r)
            
            return cur
        
        return makeTree(0, len(nums)-1)


s = Solution()
print(s.sortedArrayToBST([-10,-3,0,5,9]))