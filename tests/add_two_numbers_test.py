import unittest
from src.add_two_numbers import ListNode, AddTwo
from functools import reduce
from operator import add

class test_add_two_numbers(unittest.TestCase):
    def test_add_two_numbers(self):
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))
        adder = AddTwo()
        result = adder.addTwoNumbers(l1, l2)

        self.assertEqual(result, 807)
