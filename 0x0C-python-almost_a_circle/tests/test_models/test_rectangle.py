#!/usr/bin/python3
"""Unit tests for Rectangle class"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Base class"""

    def test_rect_creation(self):
        """Test Rectangle"""
        b1 = Rectangle(1, 2)
        self.assertEqual(b1.id, 5)
        self.assertEqual(b1.width, 1)
        self.assertEqual(b1.height, 2)
        self.assertEqual(b1.x, 0)
        self.assertEqual(b1.y, 0)

    def test_rect_str(self):
        """Test Rect"""
        with self.assertRaises(TypeError) as te:
            b2 = Rectangle("1", 2)

        self.assertEqual(str(te.exception), "width must be an integer")

    def test_rect_height(self):
        with self.assertRaises(TypeError) as te:
            b3 = Rectangle(1, "2")

        self.assertEqual(str(te.exception), "height must be an integer")

    def test_rect_x(self):
        with self.assertRaises(TypeError) as te:
            b4 = Rectangle(1, 2, "3")

        self.assertEqual(str(te.exception), "x must be an integer")

    def test_rect_x(self):
        with self.assertRaises(TypeError) as te:
            b4 = Rectangle(1, 2, 3, "4")

        self.assertEqual(str(te.exception), "y must be an integer")


if __name__ == "__main__":
    unittest.main()
