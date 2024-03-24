import unittest
from leetcode.q322 import Solution

class Test322(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            Solution().coinChange([1, 2, 5], 11),
            3
        )

    def test_2(self):
        self.assertEqual(
            Solution().coinChange([2], 3),
            -1
        )

    def test_3(self):
        self.assertEqual(
            Solution().coinChange([1], 0),
            0
        )

    def test_4(self):
        self.assertEqual(
            Solution().coinChange([1], 1),
            1
        )

    def test_5(self):
        self.assertEqual(
            Solution().coinChange([1], 2),
            2
        )

    def test_6(self):
        self.assertEqual(
            Solution().coinChange([186, 419, 83, 408], 6249),
            20
        )

if __name__ == '__main__':
    unittest.main()