import unittest
from leetcode.q2 import Solution
from leetcode.q2 import ListNode

class Test2(unittest.TestCase):
    def test_1(self):
        l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3)))
        l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4)))
        result = Solution().addTwoNumbers(l1, l2)
        self.assertEqual(7, result.val)
        self.assertEqual(0, result.next.val)
        self.assertEqual(8, result.next.next.val)

    def test_2(self):
        l1 = ListNode(val=1, next=ListNode(val=8))
        l2 = ListNode(val=0)
        result = Solution().addTwoNumbers(l1, l2)
        self.assertEqual(1, result.val)
        self.assertEqual(8, result.next.val)