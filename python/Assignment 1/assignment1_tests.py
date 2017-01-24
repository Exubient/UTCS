"""A few very basic tests for CS109 Python Assignment 1.

This does not test for all the requirements of the assignment! So make
sure you test it yourself.

Run this script using:
  python3.5 assignment1_tests.py
It should work if you are in the same directory as your assignment1.py
file. If this does not work you may want to try:
  PYTHONPATH=[directory containing assignment1.py] python3.5 assignment1_tests.py
"""

# DO NOT CHANGE THIS FILE. Grading will be done with an official
# version, so make sure your code work with this exact version.

import unittest

import assignment1

import sys
if sys.version_info[0] < 3 or (sys.version_info[0] == 3 and sys.version_info[1] < 4):
    raise Exception("Must be using Python 3.4 or greater")

class Assignment1Tests(unittest.TestCase):
    def test_fib2(self):
        self.assertEqual(assignment1.fib(2), 1)

    def test_fac0(self):
        self.assertEqual(assignment1.fac(0), 1)

    def test_fac4(self):
        self.assertEqual(assignment1.fac(4), 24)

    def test_fib1(self):
        self.assertEqual(assignment1.fib(1), 1)

    def test_fib50(self):
        self.assertEqual(assignment1.fib(15), 610)

    def test_fib30(self):
        self.assertEqual(assignment1.fib(30), 832040)

    def test_fib31(self):
        self.assertEqual(assignment1.fib(31), 1346269)

    def test_fac10(self):
        self.assertEqual(assignment1.fac(10), 3628800)

    def test_fac15(self):
        self.assertEqual(assignment1.fac(15), 1307674368000)

    def test_fac100(self):
        self.assertEqual(assignment1.fac(100), 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000)

    def test_linear_fib(self):
        # This test should finish in less than a second.
        self.assertEqual(assignment1.linear_fib(100), 354224848179261915075)

    def test_linear_fib_1(self):
        self.assertEqual(assignment1.linear_fib(1), 1)
        
    def test_linear_fib_50(self):
        self.assertEqual(assignment1.linear_fib(50), 12586269025)

    def test_linear_fib_51(self):
        self.assertEqual(assignment1.linear_fib(51), 20365011074)

if __name__ == "__main__":
    unittest.main()
