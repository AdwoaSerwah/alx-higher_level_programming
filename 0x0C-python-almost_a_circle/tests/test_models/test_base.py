#!/usr/bin/python3
"""This is a unit test for Base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """This is a test"""
    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base(None).id, 2)


if __name__ == "__main__":
    unittest.main()
