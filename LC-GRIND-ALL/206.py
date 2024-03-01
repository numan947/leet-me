# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # single element case
        if not head or head.next == None:
            return head
        
        prevNode, nextNode = head, head.next
        
        while(nextNode!=None):
            tmpNode = nextNode.next    
            nextNode.next = prevNode
            prevNode = nextNode
            nextNode = tmpNode
        head.next = None
        
        return prevNode
        