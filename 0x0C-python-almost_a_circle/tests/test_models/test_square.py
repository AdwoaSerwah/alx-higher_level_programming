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

    def test_sq_three(self):
        """Test Square 3"""
        b1 = Square(1, 2, 3, 86)
        self.assertEqual(b1.size, 1)
        self.assertEqual(b1.x, 2)
        self.assertEqual(b1.y, 3)
        self.assertEqual(b1.id, 86)


if __name__ == "__main__":
    unittest.main()
