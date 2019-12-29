#!/usr/bin/python3
"""test for db storage"""
from models.state import State
from models.engine.db_storage import DBStorage
import unittest
import MySQLdb
import pep8
import os


class TestDBStorage(unittest.TestCase):
    '''test the FileStorage'''
    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'db')
    def test_pep8_DBStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

if __name__ == "__main__":
    unittest.main()
