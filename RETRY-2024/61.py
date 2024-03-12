# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        listLength = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            listLength+=1
        
        if listLength == 0 or listLength == 1:
            return head
        k%=listLength
        if k == 0:
            return head
        
        
        def reverseList(lst:ListNode):
            tl = dummy = ListNode()
            while lst:
                hNxt = tl.next
                lNxt = lst.next

                tl.next = lst
                lst.next = hNxt
                
                lst = lNxt
            return dummy.next
        
        revFull = reverseList(head)        
        prv, lst2Head = None, revFull
        
        for _ in range(k):
            prv = lst2Head
            lst2Head = lst2Head.next
        prv.next = None
        tmpHead = revFull
        revFull = reverseList(revFull)
        lst2Head = reverseList(lst2Head)
        tmpHead.next = lst2Head
        
        return revFull


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))

s = Solution()
s.rotateRight(head, 2)

head = ListNode(1, ListNode(2))
s.rotateRight(head, 2)