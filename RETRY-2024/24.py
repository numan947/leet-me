# Definition for singly-linked list.
from ast import List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: # handle single value thingy
            return head
        dummy = ListNode()
        dummy.next = head
        f:ListNode = dummy
        s:ListNode = dummy.next
        while s and s.next:
            t1 = f.next
            t2 = s.next
            # print("Swapping: ", t1.val, t2.val)
            nxtFrst = t1
            t1.next = t2.next
            t2.next = t1
            f.next = t2
            if nxtFrst:
                f = nxtFrst
                s = nxtFrst.next
        return dummy.next
        
                