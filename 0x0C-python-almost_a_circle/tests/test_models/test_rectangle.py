#!/usr/bin/python3
"""Unit tests for Rectangle class"""
import unittest
from models.rectangle import Rectangle
from unittest.mock import patch
from unittest.mock import mock_open
from models.base import Base
import io
import os
import sys


class TestRectangle(unittest.TestCase):
    """Test cases for the Base class"""
    def test_rect_creation(self):
        """Test Rectangle 1"""
        b1 = Rectangle(1, 2)
        # self.assertEqual(b1.id, 2)
        self.assertEqual(b1.width, 1)
        self.assertEqual(b1.height, 2)
        self.assertEqual(b1.x, 0)
        self.assertEqual(b1.y, 0)

    def test_rect_again(self):
        """Test Rectangle 2"""
        b1 = Rectangle(1, 2, 3)
        # self.assertEqual(b1.id, 1)
        self.assertEqual(b1.width, 1)
        self.assertEqual(b1.height, 2)
        self.assertEqual(b1.x, 3)
        self.assertEqual(b1.y, 0)

    def test_rect_creation1(self):
        """Test Rectangle 3"""
        b1 = Rectangle(1, 2, 3, 4)
        # self.assertEqual(b1.id, 3)
        self.assertEqual(b1.width, 1)
        self.assertEqual(b1.height, 2)
        self.assertEqual(b1.x, 3)
        self.assertEqual(b1.y, 4)

    def test_rect_str(self):
        """Test Rect 4"""
        with self.assertRaises(TypeError) as te:
            b2 = Rectangle("1", 2)

        self.assertEqual(str(te.exception), "width must be an integer")

    def test_rect_height(self):
        """Test Rect 5"""
        with self.assertRaises(TypeError) as ce:
            b3 = Rectangle(1, "2")

        self.assertEqual(str(ce.exception), "height must be an integer")

    def test_rect_x(self):
        """Test Rect 6"""
        with self.assertRaises(TypeError) as se:
            b4 = Rectangle(1, 2, "3")

        self.assertEqual(str(se.exception), "x must be an integer")

    def test_rect_y(self):
        """Test Rect 7"""
        with self.assertRaises(TypeError) as ve:
            b4 = Rectangle(1, 2, 3, "4")

        self.assertEqual(str(ve.exception), "y must be an integer")

    def test_rect_correct(self):
        """Test Rect 8"""
        b1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(b1.id, 5)
        self.assertEqual(b1.width, 1)
        self.assertEqual(b1.height, 2)
        self.assertEqual(b1.x, 3)
        self.assertEqual(b1.y, 4)

    def test_rect_val_w(self):
        """Test Rect 9"""
        with self.assertRaises(ValueError) as ve:
            b4 = Rectangle(0, 2)

        self.assertEqual(str(ve.exception), "width must be > 0")

    def test_rect_val_h(self):
        """Test Rect 10"""
        with self.assertRaises(ValueError) as ve:
            b4 = Rectangle(1, 0)

        self.assertEqual(str(ve.exception), "height must be > 0")

    def test_rect_val_x(self):
        """Test Rect 11"""
        with self.assertRaises(ValueError) as ve:
            b4 = Rectangle(1, 2, -3)

        self.assertEqual(str(ve.exception), "x must be >= 0")

    def test_rect_val_y(self):
        """Test Rect 12"""
        with self.assertRaises(ValueError) as ve:
            b4 = Rectangle(1, 2, 3, -4)

        self.assertEqual(str(ve.exception), "y must be >= 0")

    def test_area(self):
        """Test Rect 13"""
        b1 = Rectangle(1, 2)
        b2 = b1.area()
        self.assertEqual(b2, 2)

    def test_rect_val_w2(self):
        """Test Rect 14"""
        with self.assertRaises(ValueError) as ve:
            b4 = Rectangle(-1, 2)

        self.assertEqual(str(ve.exception), "width must be > 0")

    def test_rect_str_rep(self):
        """Test str 15"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_no_xy(self):
        """Test display 16"""
        r = Rectangle(3, 4, 0, 0)
        result = "###\n###\n###\n###\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), result)

    def test_display_no_y(self):
        """Test display 17"""
        r = Rectangle(4, 2, 1)
        result = " ####\n ####\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), result)

    def test_display_xy(self):
        """Test display 18"""
        r = Rectangle(3, 4, 1, 2)
        result = "\n\n ###\n ###\n ###\n ###\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), result)

    def test_rect_to_dict(self):
        """19"""
        r2 = Rectangle(10, 2, 1, 9, 15)
        to_dict = {'x': 1, 'y': 9, 'id': 15, 'height': 2, 'width': 10}
        self.assertEqual(r2.to_dictionary(), to_dict)

    def test_rect_update_no_arg(self):
        """20"""
        b1 = Rectangle(10, 10, 10, 10, 10)
        b1.update()
        self.assertEqual(b1.id, 10)
        self.assertEqual(b1.width, 10)
        self.assertEqual(b1.height, 10)
        self.assertEqual(b1.x, 10)
        self.assertEqual(b1.y, 10)

    def test_rect_update_w(self):
        """21"""
        b1 = Rectangle(10, 10, 10, 10, 10)
        b1.update(89)
        self.assertEqual(b1.id, 89)
        self.assertEqual(b1.width, 10)
        self.assertEqual(b1.height, 10)
        self.assertEqual(b1.x, 10)
        self.assertEqual(b1.y, 10)

    def test_rect_update_wh(self):
        """22"""
        b1 = Rectangle(10, 10, 10, 10, 10)
        b1.update(89, 1)
        self.assertEqual(b1.id, 89)
        self.assertEqual(b1.width, 1)
        self.assertEqual(b1.height, 10)
        self.assertEqual(b1.x, 10)
        self.assertEqual(b1.y, 10)

    def test_rect_update_whx(self):
        """23"""
        b1 = Rectangle(10, 10, 10, 10, 10)
        b1.update(89, 1, 2)
        self.assertEqual(b1.id, 89)
        self.assertEqual(b1.width, 1)
        self.assertEqual(b1.height, 2)
        self.assertEqual(b1.x, 10)
        self.assertEqual(b1.y, 10)

    def test_rect_update_whxy(self):
        """24"""
        b1 = Rectangle(10, 10, 10, 10, 10)
        b1.update(89, 1, 2, 3)
        self.assertEqual(b1.id, 89)
        self.assertEqual(b1.width, 1)
        self.assertEqual(b1.height, 2)
        self.assertEqual(b1.x, 3)
        self.assertEqual(b1.y, 10)

    def test_rect_update_whxyi(self):
        """25"""
        b1 = Rectangle(10, 10, 10, 10, 10)
        b1.update(89, 1, 2, 3, 4)
        self.assertEqual(b1.id, 89)
        self.assertEqual(b1.width, 1)
        self.assertEqual(b1.height, 2)
        self.assertEqual(b1.x, 3)
        self.assertEqual(b1.y, 4)

    def test_rect_create_id(self):
        """26"""
        b1 = Rectangle.create(**{'id': 89})
        self.assertEqual(b1.id, 89)
        self.assertEqual(b1.width, 1)
        self.assertEqual(b1.height, 1)
        self.assertEqual(b1.x, 0)
        self.assertEqual(b1.y, 0)

    def test_rect_create_iw(self):
        """27"""
        b1 = Rectangle.create(**{'id': 89, 'width': 2})
        self.assertEqual(b1.id, 89)
        self.assertEqual(b1.width, 2)
        self.assertEqual(b1.height, 1)
        self.assertEqual(b1.x, 0)
        self.assertEqual(b1.y, 0)

    def test_rect_create_iwh(self):
        """28"""
        b1 = Rectangle.create(**{'id': 89, 'width': 2, 'height': 3})
        self.assertEqual(b1.id, 89)
        self.assertEqual(b1.width, 2)
        self.assertEqual(b1.height, 3)
        self.assertEqual(b1.x, 0)
        self.assertEqual(b1.y, 0)

    def test_rect_create_iwhx(self):
        """29"""
        b1 = Rectangle.create(**{'id': 89, 'width': 2, 'height': 3, 'x': 4})
        self.assertEqual(b1.id, 89)
        self.assertEqual(b1.width, 2)
        self.assertEqual(b1.height, 3)
        self.assertEqual(b1.x, 4)
        self.assertEqual(b1.y, 0)

    def test_rect_create_iwhxy(self):
        """30"""
        b1 = Rectangle.create(**{
            'id': 89, 'width': 2, 'height': 3, 'x': 4, 'y': 5})
        self.assertEqual(b1.id, 89)
        self.assertEqual(b1.width, 2)
        self.assertEqual(b1.height, 3)
        self.assertEqual(b1.x, 4)
        self.assertEqual(b1.y, 5)

    def setUp(self):
        """Set up for testing"""
        # Backup existing file
        self.backup_filename = "Rectangle_backup.json"
        if os.path.exists("Rectangle.json"):
            os.rename("Rectangle.json", self.backup_filename)

    def tearDown(self):
        """Clean up after testing"""
        # Restore the backup file
        if os.path.exists(self.backup_filename):
            os.rename(self.backup_filename, "Rectangle.json")

    def test_save_to_file_none(self):
        """Test save_to_file_json with None 31"""
        with patch('builtins.open', new_callable=mock_open) as mock_file:
            Rectangle.save_to_file(None)

        # Check if open was called with the correct arguments
        mock_file.assert_called_once_with(
                'Rectangle.json', 'w', encoding="utf-8")

        # Check if write was called with the correct argument
        mock_file().write.assert_called_once_with('[]')

    def test_load_from_file_none(self):
        """Test load_from_file_json with None 32"""
        result = Rectangle.load_from_file()

        # Check if an empty list is returned
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
