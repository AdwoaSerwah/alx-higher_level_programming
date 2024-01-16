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
        with self.assertRaises(TypeError) as ce:
            b3 = Rectangle(1, "2")

        self.assertEqual(str(ce.exception), "height must be an integer")

    def test_rect_x(self):
        with self.assertRaises(TypeError) as se:
            b4 = Rectangle(1, 2, "3")

        self.assertEqual(str(se.exception), "x must be an integer")

    def test_rect_x(self):
        with self.assertRaises(TypeError) as ve:
            b4 = Rectangle(1, 2, 3, "4")

        self.assertEqual(str(ve.exception), "y must be an integer")

    def test_rect_correct(self):
        b1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(b1.id, 5)
        self.assertEqual(b1.width, 1)
        self.assertEqual(b1.height, 2)
        self.assertEqual(b1.x, 3)
        self.assertEqual(b1.y, 4)

    def test_rect_val_w(self):
        with self.assertRaises(ValueError) as ve:
            b4 = Rectangle(0, 2)

        self.assertEqual(str(ve.exception), "width must be > 0")

    def test_rect_val_h(self):
        with self.assertRaises(ValueError) as ve:
            b4 = Rectangle(1, 0)

        self.assertEqual(str(ve.exception), "height must be > 0")

    def test_rect_val_x(self):
        with self.assertRaises(ValueError) as ve:
            b4 = Rectangle(1, 2, -3)

        self.assertEqual(str(ve.exception), "x must be >= 0")

    def test_rect_val_y(self):
        with self.assertRaises(ValueError) as ve:
            b4 = Rectangle(1, 2, 3, -4)

        self.assertEqual(str(ve.exception), "y must be >= 0")


if __name__ == "__main__":
    unittest.main()
