from platform import node
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyMap = {} # (maps original -> copy)
        
        ## Straightforward recursive way
        # def copyRec(cur:Node):
        #     if cur == None:
        #         return None
        #     if cur in copyMap: # already created a copy
        #         return copyMap[cur]
        #     newCopy = Node(cur.val)
        #     copyMap[cur] = newCopy
        #     newCopy.next = copyRec(cur.next)
        #     newCopy.random = copyRec(cur.random)
        #     return newCopy
                
        # return copyRec(head)
        
        ## Another way -> two pass: first copy the entire linkedlist, then add the random pointers
        if not head:
            return None
        
        cur = head
        # create a copy
        while cur:
            copyMap[cur] = Node(cur.val)
            cur = cur.next
        
        # now add the connections
        cur = head
        
        while cur:
            copyMap[cur].next = copyMap[cur.next] if cur.next else None
            copyMap[cur].random = copyMap[cur.random] if cur.random else None
            cur = cur.next
        return copyMap[head]
            
        

        
        
