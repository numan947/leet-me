# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        p1 = dummy
        p2 = dummy
        
        for i in range(n):
            p1 = p1.next
        
        
        while p1.next != None:
            p1 = p1.next
            p2 = p2.next
        
        
        p2.next = p2.next.next
        
        return dummy.next