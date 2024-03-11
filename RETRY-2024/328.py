# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: # 0 and 1 node
            return head
        dummyOdd = ListNode()
        dummyOddLast = dummyOdd
        dummyEven = ListNode()
        dummyEvenLast = dummyEven
        
        cur = 1
        ll = head
        while ll:
            if cur%2:
                dummyOddLast.next = ll
                dummyOddLast = ll
            else:
                dummyEvenLast.next = ll
                dummyEvenLast = ll
            cur+=1
            ll = ll.next
        
        dummyEvenLast.next = None
        dummyOddLast.next = dummyEven.next
        return dummyOdd.next