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

    def test_sq_size_zero(self):
        """11"""
        with self.assertRaises(ValueError) as ve:
            b1 = Square(0)
        self.assertEqual(str(ve.exception), "width must be > 0")

    def test_sq_str(self):
        """12"""
        b1 = Square(1, 2, 3, 4)
        self.assertEqual(str(b1), "[Square] (4) 2/3 - 1")

    def test_sq_to_dict(self):
        """13"""
        r2 = Square(10, 2, 1, 9)
        to_dict = {'x': 2, 'y': 1, 'id': 9, 'size': 10}
        self.assertEqual(r2.to_dictionary(), to_dict)

    def test_sq_update_no_arg(self):
        """14"""
        b1 = Square(10, 10, 10, 10)
        b1.update()
        self.assertEqual(b1.id, 10)
        self.assertEqual(b1.size, 10)
        self.assertEqual(b1.x, 10)
        self.assertEqual(b1.y, 10)

    def test_sq_update_i(self):
        """15"""
        b1 = Square(10, 10, 10, 10,)
        b1.update(89)
        self.assertEqual(b1.id, 89)
        self.assertEqual(b1.size, 10)
        self.assertEqual(b1.x, 10)
        self.assertEqual(b1.y, 10)

    def test_sq_update_is(self):
        """16"""
        b1 = Square(10, 10, 10, 10)
        b1.update(89, 1)
        self.assertEqual(b1.id, 89)
        self.assertEqual(b1.size, 1)
        self.assertEqual(b1.x, 10)
        self.assertEqual(b1.y, 10)

    def test_sq_update_isx(self):
        """17"""
        b1 = Square(10, 10, 10, 10)
        b1.update(89, 1, 2)
        self.assertEqual(b1.id, 89)
        self.assertEqual(b1.size, 1)
        self.assertEqual(b1.x, 2)
        self.assertEqual(b1.y, 10)

    def test_sq_update_isxy(self):
        """18"""
        b1 = Square(10, 10, 10, 10)
        b1.update(89, 1, 2, 3)
        self.assertEqual(b1.id, 89)
        self.assertEqual(b1.size, 1)
        self.assertEqual(b1.x, 2)
        self.assertEqual(b1.y, 3)

    def test_sq_create_id(self):
        """19"""
        b1 = Square.create(**{'id': 89})
        self.assertEqual(b1.id, 89)
        self.assertEqual(b1.size, 1)
        self.assertEqual(b1.x, 0)
        self.assertEqual(b1.y, 0)

    def test_sq_create_is(self):
        """20"""
        b1 = Square.create(**{'id': 89, 'size': 2})
        self.assertEqual(b1.id, 89)
        self.assertEqual(b1.size, 2)
        self.assertEqual(b1.x, 0)
        self.assertEqual(b1.y, 0)

    def test_sq_create_ish(self):
        """21"""
        b1 = Square.create(**{'id': 89, 'size': 2, 'x': 3})
        self.assertEqual(b1.id, 89)
        self.assertEqual(b1.size, 2)
        self.assertEqual(b1.x, 3)
        self.assertEqual(b1.y, 0)

    def test_sq_create_isxy(self):
        """22"""
        b1 = Square.create(**{'id': 89, 'size': 2, 'x': 3, 'y': 4})
        self.assertEqual(b1.id, 89)
        self.assertEqual(b1.size, 2)
        self.assertEqual(b1.x, 3)
        self.assertEqual(b1.y, 4)


if __name__ == "__main__":
    unittest.main()
