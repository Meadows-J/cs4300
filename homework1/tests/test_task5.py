#imports for file path
import sys
import os

#get the file path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import pytest
from task5 import favBooks, studentDatabase



def testfavBooksList():
    assert isinstance(favBooks, list)


def testfavBooksLen():
    assert len(favBooks) == 5



def testFirstThree():
    first_three = favBooks[:3]
    assert len(first_three) == 3
    assert first_three[0] == ("Percy Jackson", "Rick Riordan")
    assert first_three[1] == ("The Witcher", "Andrzej Sapkowski")
    assert first_three[2] == ("The Great Gatsby", "F. Scott Fitzgerald")

def testIsDict():
    assert isinstance(studentDatabase, dict)

def testLookup():
    assert studentDatabase["Alice Johnson"] == "S1001"


def testStudentNames():
    assert "Diana Prince" in studentDatabase

