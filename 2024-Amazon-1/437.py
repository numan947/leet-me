# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        sumCounter = defaultdict(int)
        sumCounter[0] = 1 # initially 0 is the sum and without taking anything
        
        def dfs(node, running_sum):
            if not node:
                return 0
            
            running_sum += node.val
            #possible paths
            possible_path_counts = sumCounter[running_sum - targetSum]
            
            
            # increase the count of the running sum
            sumCounter[running_sum]+=1
            
            # dfs
            possible_path_counts += dfs(node.left, running_sum)
            possible_path_counts += dfs(node.right, running_sum)
            
            sumCounter[running_sum]-=1
            
            return possible_path_counts
        
        return dfs(root, 0)
