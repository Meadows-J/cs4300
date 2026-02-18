#imports for file path
import sys
import os

#get the file path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import pytest
from task4 import calculate_discount


# Test with two integers
def testcalculate_discountTwoInts():
    assert calculate_discount(100, 10) == 1000


# Test with int price and float discount
def testcalculate_discountIntToFLoat():
    assert calculate_discount(100, 0.10) == 10.0


# Test with two floats
def testcalculate_discountTwoFloats():
    assert calculate_discount(100.1, 0.10) == 10.01


# Test with float price and int discount
def test_calculate_discountFloatToInt():
    assert calculate_discount(100.5, 2) == 201.0
