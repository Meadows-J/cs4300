#imports for file path
import sys
import os

#get the file path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from task1 import hellowWorld

def testHellow(capsys):
    hellowWorld()
    captured = capsys.readouterr()
    assert captured.out == "Hello World!\n"