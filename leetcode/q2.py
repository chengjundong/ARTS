from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # first node
        result = ListNode(val=l1.val+l2.val)

        if result.val >= 10:
            result.val -= 10
            result.next = ListNode(val=1)

        l1next = l1.next
        l2next = l2.next
        l3 = result
        while l1next is not None or l2next is not None or l3 is not None:
            l3 = self._add(l1next, l2next, l3)
            if l3 is not None and l3.val >= 10:
                l3.val -= 10
                l3.next = ListNode(val=1)
            l1next = l1next.next if l1next is not None else None
            l2next = l2next.next if l2next is not None else None

        return result
    
    def _add(self, l1: Optional[ListNode], l2: Optional[ListNode], l3: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return l3.next
        elif l1 is None:
            if l3.next is None:
                l3.next = ListNode(val=l2.val)
            else:
                l3.next.val += l2.val
            return l3.next
        elif l2 is None:
            if l3.next is None:
                l3.next = ListNode(val=l1.val)
            else:
                l3.next.val += l1.val
            return l3.next
        else:
            if l3.next is None:
                l3.next = ListNode(val=l1.val + l2.val)
            else:
                l3.next.val += (l1.val + l2.val)
            return l3.next