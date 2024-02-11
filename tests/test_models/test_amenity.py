#!/usr/bin/python3
"""unittest for Amenity calss"""
import unittest

from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """testcase for Amenity class"""

    def setUp(self):
        self.amenity = Amenity()

    def test_amenity(self):
        self.assertTrue(issubclass(type(self.amenity), BaseModel))

    def test_attr(self):
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_class_attr(self):
        self.assertIs(type(self.amenity.name), str)
        self.assertFalse(bool(getattr(self.amenity, "name")))


if __name__ == "__main__":
    unittest.main()
