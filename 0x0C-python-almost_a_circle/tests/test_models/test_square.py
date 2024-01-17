#!/usr/bin/python3
"""Unit tests for Square class"""
import unittest
import json
from models.rectangle import Rectangle
from unittest.mock import patch
from unittest.mock import mock_open
from models.base import Base
from models.square import Square
import io
import os
import sys


class TestSquare(unittest.TestCase):
    """Test cases for the Base class"""
    def test_sq_one(self):
        """Test Square 1"""
        b1 = Square(1)
        self.assertEqual(b1.size, 1)
        self.assertEqual(b1.x, 0)
        self.assertEqual(b1.y, 0)

    def test_sq_two(self):
        """Test Square 2"""
        b1 = Square(1, 2)
        self.assertEqual(b1.size, 1)
        self.assertEqual(b1.x, 2)
        self.assertEqual(b1.y, 0)

    def test_sq_three(self):
        """Test Square 3"""
        b1 = Square(1, 2, 3)
        self.assertEqual(b1.size, 1)
        self.assertEqual(b1.x, 2)
        self.assertEqual(b1.y, 3)

    def test_sq_four(self):
        """Test Square 4"""
        b1 = Square(1, 2, 3, 86)
        self.assertEqual(b1.size, 1)
        self.assertEqual(b1.x, 2)
        self.assertEqual(b1.y, 3)
        self.assertEqual(b1.id, 86)

    def test_sq_size_type(self):
        """5"""
        with self.assertRaises(TypeError) as te:
            b1 = Square("1")
        self.assertEqual(str(te.exception), "width must be an integer")

    def test_sq_x_type(self):
        """6"""
        with self.assertRaises(TypeError) as te:
            b1 = Square(1, "2")
        self.assertEqual(str(te.exception), "x must be an integer")

    def test_sq_y_type(self):
        """7"""
        with self.assertRaises(TypeError) as te:
            b1 = Square(1, 2, "3")
        self.assertEqual(str(te.exception), "y must be an integer")

    def test_sq_size_val(self):
        """8"""
        with self.assertRaises(ValueError) as ve:
            b1 = Square(-1)
        self.assertEqual(str(ve.exception), "width must be > 0")

    def test_sq_x_val(self):
        """9"""
        with self.assertRaises(ValueError) as ve:
            b1 = Square(1, -2)
        self.assertEqual(str(ve.exception), "x must be >= 0")

    def test_sq_y_val(self):
        """10"""
        with self.assertRaises(ValueError) as ve:
            b1 = Square(1, 2, -3)
        self.assertEqual(str(ve.exception), "y must be >= 0")


if __name__ == "__main__":
    unittest.main()
