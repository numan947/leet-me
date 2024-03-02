# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution: ## NOTE: my 3 pointer method for solving linked list almost always works --> prv, cur, nxt
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next == None: ## base case
            return head
        
        prv:ListNode = None
        cur:ListNode = head
        nxt:ListNode = head.next
        
        while cur:
            cur.next = prv
            
            prv = cur
            cur = nxt
            if nxt:
                nxt = nxt.next
        
        return prv