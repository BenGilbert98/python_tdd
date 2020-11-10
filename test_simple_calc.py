# This file will have our tests written

# importing required modules for unit testing
from simple_calc import Simple_Calc
import unittest
import pytest


# Lets create a class to write our tests

class Calc_Test(unittest.TestCase):
    # unittest.TestCase works with unittest framework as a parent class
    calc = Simple_Calc()

    # Creating object of class

    # IMPORTANT - we MUST use test word in our functions so python interpreter knows what we are testing
    # asking python to check whether 2 + 4 = 6. If true, test is passed. If false, test fails
    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 6)

    # Tests if 4-2 is 2. If true, test is passed. If false, test fails
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    # Tests if 4 * 2 is 8. If true, test is passed. If false, test fails
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 2), 8)

    # Tests if 4 / 2 is 2. If true, test is passed. If false, test fails
    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 2), 2)
