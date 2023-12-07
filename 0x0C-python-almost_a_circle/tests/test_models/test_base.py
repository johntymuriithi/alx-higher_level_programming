#!/usr/bin/python3

import json
import unittest
from models import base

Base = base.Base

class TestBase(unittest.TestCase):

        def test_id(self):
            basee = Base(15)

            self.assertEqual(basee.id, 15)

if __name__ == '__main__':
    unittest.main()
