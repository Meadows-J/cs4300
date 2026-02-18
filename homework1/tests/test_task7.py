#imports for file path
import sys
import os

#get the file path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import numpy as np
from task7 import createArrays, addArrays, subtractArrays

def testcreateArrays():
    arr1, arr2 = createArrays()

    assert isinstance(arr1, np.ndarray)
    assert isinstance(arr2, np.ndarray)
    assert np.array_equal(arr1, np.array([1, 2, 3, 4]))
    assert np.array_equal(arr2, np.array([4, 3, 2, 1]))


def test_add_arrays():
    arr1, arr2 = createArrays()
    result = addArrays(arr1, arr2)

    expected = np.array([5, 5, 5, 5])
    assert np.array_equal(result, expected)


def test_subtract_arrays():
    arr1, arr2 = createArrays()
    result = subtractArrays(arr1, arr2)

    expected = np.array([-3, -1, 1, 3])
    assert np.array_equal(result, expected)