# TDD (Test Driven Development)
TDD is a practice where you create the test 1st and then the code in order to pass those tests.
![](images/TDD_diagram.png)
## Type of testing
- Unit Testing
- TDD

## Modules to help test code
- pytest (``` pip install pytest```) in terminal
- unittest (including in python already)

## Why do we use TDD?
- To make sure the code is functioning properly before it is shipped
- Helps us minimise the risk of failure before sending product to production

## Steps
- Create a file to write our tests
- Create a file to write test code
- Run the tests (it will fail)
- Refactor and add code to pass the tests

- Create the tests to fail (self.assertEqual(<function_name>) is used to check if a calculation will work)
```
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
```
- run the test (Expected to fail)
- Create the Simple_Calc class
```
class Simple_Calc:

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2
```
- re run the test (Expected to pass)
#### **Naming Convention**
- file name: simple_calc
- test file name: test_simple_calc

#### **Function Names**
- test function names must start with "test" so that Python can recognise it as a test function

## pytest

- pytest looks for files with ```test_*.py``` and  ```_test*.py```
- we can use different conditions with assertEqual as per need

## pytest commands
- ```python -m unittest discover -v``` 
- ```python -m pytest ```
- ```-v```  - verbose flag (more information on the test)