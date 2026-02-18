#imports for file path
import sys
import os

#get the file path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

# tests/test_task_types.py

from task2 import (
    multiplyIntFloat,
    reverseString,
    booleanAnd,
    booleanOr
)


def testMultiplyIntFloat():
    result = multiplyIntFloat()
    assert result == 1.1
    assert isinstance(result, float)


def testReverseString():
    result = reverseString()
    assert result == "tset"
    assert isinstance(result, str)


def testBooleanAnd():
    result = booleanAnd()
    assert result is False
    assert isinstance(result, bool)


def testBooleanOr():
    result = booleanOr()
    assert result is True
    assert isinstance(result, bool)
