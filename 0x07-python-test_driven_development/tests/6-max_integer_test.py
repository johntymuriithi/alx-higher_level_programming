#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_none(self):
        self.assertEqual(max_integer(), None)


    def test_string(self):
        self.assertRaises(TypeError, max_integer, [4, 'john', 5])

    def test_1(self):
        self.assertEqual(max_integer([1]), 1)

    def test_2(self):
        self.assertEqual(max_integer([2, 5]), 5)

    def test_3(self):
        self.assertEqual(max_integer([5 ,67, 6]), 67)

if __name__ == '__main__':
    unittest.main()
