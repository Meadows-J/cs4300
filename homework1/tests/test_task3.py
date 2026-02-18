#imports for file path
import sys
import os

#get the file path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from task3 import numCheck, primeCheck

#The check nums test
def testNumCheckPos():
    assert numCheck(5) == "Positive"

def testNumCheckNeg():
    assert numCheck(-3) == "Negitive"
def testNumCheckZero():
    assert numCheck(0) == "Zero"

#check the prime nums
def testPrimeCheckPrimes():
    assert primeCheck(2) is True
    assert primeCheck(3) is True
    assert primeCheck(13) is True

def testPrimeCheckPrimesNon():
    assert primeCheck(4) is False
    assert primeCheck(9) is False



def testFirstPrimes():
    primeList = []
    counter = 2

    while len(primeList) < 10:
        if primeCheck(counter):
            primeList.append(counter)
        counter += 1

    assert primeList == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


#check the sums
def testSum():
    whileCounter = 0
    total = 0

    while whileCounter < 101:
        total += whileCounter
        whileCounter += 1

    assert total == 5050
