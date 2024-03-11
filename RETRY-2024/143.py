# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if not head or not head.next:
            return
        
        
        def findMid(lst:ListNode):
            slowPrev = None
            slow = lst
            fast = lst
            while fast and fast.next:
                slowPrev = slow
                slow = slow.next
                fast = fast.next.next
            return slow, slowPrev
        
        def reverseList(lst:ListNode):
            dummy = ListNode()
            
            while lst:
                tmp = lst.next
                dtmp = dummy.next
                
                dummy.next = lst
                lst.next = dtmp
                lst = tmp
            return dummy.next
        
        mid,midPrev = findMid(head)
        
        midPrev.next = None
        lst1 = head
        lst2 = mid
        lst2 = reverseList(lst2)
        
        tail= dummy = ListNode()
        
        while lst1 and lst2:
            tmp1 = lst1.next
            tmp2 = lst2.next
            
            lst1.next = tail.next
            tail.next = lst1
            tail = lst1
            
            lst2.next = tail.next
            tail.next = lst2
            tail = lst2
            
            lst1 = tmp1
            lst2 = tmp2
        
        while lst2:
            tmp2 = lst2.next
            lst2.next = tail.next
            tail.next = lst2
            tail = lst2
            lst2 = tmp2
        
            
            