#!/usr/bin/python3
"""Unit tests for the Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_base_creation(self):
        """Test the creation of Base instances."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_base_with_id(self):
        """Test the creation of Base instances with a specified id."""
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_base_nb_objects(self):
        """Test the private class attribute __nb_objects."""
        b5 = Base()
        self.assertEqual(type(b5)._Base__nb_objects, 4)

    def test_base_to_json_string(self):
        """Test something"""
        me = Base.to_json_string(None)
        self.assertEqual(me, '[]')


if __name__ == "__main__":
    unittest.main()
