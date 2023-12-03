#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """Tests the function max_integer
    def test_type(self):
        # Check if data type is list
        self.assertRaises(TypeError, max_integer, 1)
        self.assertRaises(TypeError, max_integer, ["w"])
        self.assertRaises(TypeError, max_integer, [1, "w"])
        self.assertRaises(TypeError, max_integer, [1, []])
        self.assertRaises(TypeError, max_integer, [[]])
        self.assertRaises(TypeError, max_integer, "w")
    """

    def test_empty_list(self):
        """Test if list is empty"""
        self.assertEqual(max_integer([]), None)

    def test_no_args(self):
        """Test if no argument"""
        self.assertEqual(max_integer(), None)

    def test_integers(self):
        """Test integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([1, 1]), 1)
        self.assertEqual(max_integer([-1, - 2, -3, -4]), -1)
        self.assertEqual(max_integer([2]), 2)


if __name__ == "__main__":
    unittest.main()
