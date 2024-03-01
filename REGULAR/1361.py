from typing import List
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        par = [i for i in range(n)]
        rank = [1]*n
        
        def findParent(nd):
            while(par[nd]!=nd):
                par[nd] = par[par[nd]]
                nd = par[nd]
            return nd
        
        def union(n1, n2):
            p1, p2 = findParent(n1), findParent(n2)
            if p1 == p2:
                return False
            par[p2] = p1
            rank[p1] += rank[p2]

            return True
        
        totalSize = n
        
        for i in range(n):
            node = i
            left = leftChild[i]
            right = rightChild[i]
            
            if left != -1:
                if findParent(left) != left: # left has a parent other than node
                    print("H")
                    return False
                if(not union(node, left)):
                    return False
                else:
                    totalSize -= 1
            if right != -1:
                if findParent(right) !=right:
                    print("H", node, right)
                    print(findParent(right))
                    return False
                if(not union(node, right)):
                    return False
                else:
                    totalSize -= 1
        return totalSize == 1
    

s = Solution()

print(s.validateBinaryTreeNodes(4,
[3,-1,1,-1],
[-1,-1,0,-1]))