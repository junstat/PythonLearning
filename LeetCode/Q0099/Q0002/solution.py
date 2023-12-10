from typing import Optional

from LeetCode.datastructure.list_node import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        p = dummy
        while l1 is not None or l2 is not None:
            a = l1.val if l1 is not None else 0
            b = l2.val if l2 is not None else 0
            carry += a + b
            p.next = ListNode(carry % 10)
            p = p.next
            carry //= 10
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        if carry > 0:
            p.next = ListNode(carry)
        return dummy.next
