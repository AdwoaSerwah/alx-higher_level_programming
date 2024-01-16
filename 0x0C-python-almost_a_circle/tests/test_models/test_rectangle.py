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


if __name__ == "__main__":
    unittest.main()
