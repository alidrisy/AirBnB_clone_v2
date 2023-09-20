import uuid
import os
import sys
import unittest
from io import StringIO
from unittest.mock import patch, Mock
from console import HBNBCommand
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import console


class TestConsole(unittest.TestCase):
    """Test class implementation for console.

    Args:
        unittest (_type_): _description_
    """

    def test_module_doc(self):
        """Test for module documentation"""
        self.assertIsNotNone(console.__doc__)

    def test_class_doc(self):
        """Test for class documentation"""
        self.assertIsNotNone(HBNBCommand.__doc__)

    def test_method_docs(self):
        """Test all methods in ``console`` for docs"""
        methods = [
            HBNBCommand.do_EOF,
            HBNBCommand.help_EOF,
            HBNBCommand.do_quit,
            HBNBCommand.help_quit,
            HBNBCommand.emptyline,
            HBNBCommand.do_create,
            HBNBCommand.help_create,
            HBNBCommand.do_show,
            HBNBCommand.help_show,
            HBNBCommand.do_destroy,
            HBNBCommand.help_destroy,
            HBNBCommand.do_all,
            HBNBCommand.help_all,
            HBNBCommand.do_update,
            HBNBCommand.default,
        ]
        for meth in methods:
            self.assertIsNotNone(meth.__doc__)

    def test_quit(self):
        """Test quit method"""
        pass

    def test_empty_line(self):
        """Test empty_line method"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_help_create(self):
        """Test help_create method"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)

    def test_help_show(self):
        """Test help_show method"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)

    def test_help_destroy(self):
        """Test help_destroy method"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)

    def test_help_all(self):
        """Test help_all method"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)

    def test_help_update(self):
        """Test help_update method"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)


if __name__ == "__main__":
    unittest.main()
