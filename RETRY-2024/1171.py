# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        seenMap = {0:dummy}
        
        curSum = 0
        tmp = head
        
        while tmp:
            curSum += tmp.val
            
            # check if we saw this sum before
            if curSum in seenMap:
                node = seenMap[curSum]
                # remove all the sum seen between these nodes
                tmpSum = curSum
                delNode = node.next
                while delNode!=tmp:
                    # print("deleting..", delNode.val)
                    if (tmpSum + delNode.val) in seenMap:
                        # print("deleting..", tmpSum+delNode.val)
                        del seenMap[(tmpSum + delNode.val)]
                    tmpSum+=delNode.val
                    delNode = delNode.next
                node.next = tmp.next
                
            else:
                seenMap[curSum] = tmp
            tmp = tmp.next
        
        
        t = dummy.next
        return dummy.next

head = ListNode(0, ListNode(-1, ListNode(1)))
head2 = ListNode(1,ListNode(3,ListNode(2,ListNode(-3,ListNode(-2,ListNode(5,ListNode(5,ListNode(-5,ListNode(1)))))))))

s = Solution()
# s.removeZeroSumSublists(head)
s.removeZeroSumSublists(head2)