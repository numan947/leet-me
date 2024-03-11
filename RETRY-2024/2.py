# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = head = ListNode(0)
        
        carry = 0
        while l1 or l2:
            tmpSum = 0
            if l1:
                tmpSum+=l1.val
                l1 = l1.next
            if l2:
                tmpSum+=l2.val
                l2 = l2.next
            
            tmpSum+=carry
            carry = 0
            
            digit = tmpSum%10
            carry = tmpSum//10
            head.val = digit
            
            if l1 or l2 or carry:
                head.next = ListNode(0)
                head = head.next
        
        if carry:
            head.val = carry
        
        return result
        
        