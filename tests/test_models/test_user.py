#!/usr/bin/python3
"""
TestUserDocs classes
"""

from datetime import datetime
import inspect
from models import user
from models.base_model import BaseModel
import pep8
import unittest
User = user.User


class TestUserDocs(unittest.TestCase):
    """Tests that checks the documentation/
    User class style"""
    @classmethod
    def setUpClass(cls):
        """setting up documentation tests"""
        cls.user_f = inspect.getmembers(User, inspect.isfunction)

    def test_pep8_conformance_user(self):
        """tests whether user.py conforms to PEP8 style guide."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found codestyle errors.")

    def test_pep8_conformance_test_user(self):
        """Test whether test_user.py conforms to PEP8 style guide."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors.")

    def test_user_module_docstring(self):
        """Test whether user.py module has docstring"""
        self.assertIsNot(user.__doc__, None,
                         "user.py requires a docstring")
        self.assertTrue(len(user.__doc__) >= 1,
                        "user.py reequires a docstring")

    def test_user_class_docstring(self):
        """Test whether City class docstring"""
        self.assertIsNot(User.__doc__, None,
                         "User class needs a docstring")
        self.assertTrue(len(User.__doc__) >= 1,
                        "User class needs a docstring")

    def test_user_func_docstrings(self):
        """Test whether docstrings are present in User methods"""
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestUser(unittest.TestCase):
    """Test User class"""
    def test_is_subclass(self):
        """Test whether User is a subclass of BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_email_attr(self):
        """Test whether user has attribute email,
        and that it's an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")

    def test_password_attr(self):
        """Test whether user has attribute password,
        and it is an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")

    def test_first_name_attr(self):
        """Test whether user has attribute first_name,
        and it's an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")

    def test_last_name_attr(self):
        """Test whether user has attribute last_name,
        and it's an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method whether it creates
        a dictionary with proper attrs"""
        k = User()
        new_d = k.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in k.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test whether values in dict
        returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        k = User()
        new_d = k.to_dict()
        self.assertEqual(new_d["__class__"], "User")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], k.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], k.updated_at.strftime(t_format))

    def test_str(self):
        """test whetherthe str method has  correct output"""
        user = User()
        string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(string, str(user))
