# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
import math

from Triangle import classifyTriangle
from screen_brand import my_brand 

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    my_brand("HW02a -- Testing A Legacy Program")
    
    # define multiple sets of tests as functions with names that begin
    def testInputValues1(self):
        self.assertEqual(classifyTriangle(201, 4, 5), "InvalidInput", "Side A is above threshold, should return InvalidInput")

    def testInputValues2(self):
        self.assertEqual(classifyTriangle(3, 201, 5), "InvalidInput", "Side B is above threshold, should return InvalidInput")
    
    def testInputValues3(self):
        self.assertEqual(classifyTriangle(3, 4, 201), "InvalidInput", "Side C is above threshold, should return InvalidInput")

    def testInputValues4(self):
        self.assertEqual(classifyTriangle(-1, 4, 5), "InvalidInput", "Side A is negative, should return InvalidInput")

    def testInputValues5(self):
        self.assertEqual(classifyTriangle(3, -1, 5), "InvalidInput", "Side B is negative, should return InvalidInput")
    
    def testInputValues6(self):
        self.assertEqual(classifyTriangle(3, 4, -1), "InvalidInput", "Side C is negative, should return InvalidInput")

    def testInputTypes1(self):
        self.assertEqual(classifyTriangle("string", 4, 5), "InvalidInput", "Side A is type string, should return Invalid Input")

    def testInputTypes2(self):
        self.assertEqual(classifyTriangle(3, [], 5), "InvalidInput", "Side B is type list, should return Invalid Input") 

    def testInputTypes3(self):
        self.assertEqual(classifyTriangle(3, 4, {}), "InvalidInput", "Side C is type dictionary, should return Invalid Input")

    def testValidTriangle1(self):
        self.assertEqual(classifyTriangle(10, 4, 5), "NotATriangle", "Side A is greater than sum of Side B and Side C, should return NotATriangle")

    def testValidTriangle2(self):
        self.assertEqual(classifyTriangle(3, 10, 5), "NotATriangle", "Side B is greater than sum of Side A and Side C, should return NotATrianlge") 

    def testValidTriangle3(self):
        self.assertEqual(classifyTriangle(3, 4, 10), "NotATriangle", "Side C is greater than sum of Side A and Side B, should return NotATriangle")

    def testEquilateralTriangle(self):
        self.assertEqual(classifyTriangle(5, 5, 5), "Equilateral", "Sides form a valid equilateral triangle, should return Equilateral")
    
    def testIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(5, 5, 3), "Isosceles", "Sides form a valid isosceles triangle, should return Isosceles") 

    def testIsoscelesRightTriangle(self):
        self.assertEqual(classifyTriangle(3, 3, 3*math.sqrt(2)), "IsoscelesRight", "Sides form a valid isosceles right triangle, should return IsoscelesRight") 

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(4, 5, 6), "Scalene", "Sides form a valid scalene triangle, should return Scalene") 

    def testScaleneRightTriangle(self):
        self.assertEqual(classifyTriangle(5, 12, 13), "ScaleneRight", "Sides form a valid scalene right triangle, should return ScaleneRight")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
