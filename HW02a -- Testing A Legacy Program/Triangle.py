# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""
import math
def classifyTriangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """

    # verify that all 3 inputs are integers or float
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if((not isinstance(a,int) and not isinstance(a, float)) or (not isinstance(b,int) and not isinstance(b, float)) or (not isinstance(c,int) and not isinstance(c, float))):
        return 'InvalidInput';

    # require that the input values be >= 0 and <= 200
    if(a > 200 or b > 200 or c > 200):
        return 'InvalidInput'
        
    if(a <= 0 or b <= 0 or c <= 0):
        return 'InvalidInput'
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if ((a >= b + c) or (b >= a + c) or (c >= a + b)):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if(a == b and b == c and a == c):
        return 'Equilateral'
    elif(a == b or b == c or a == c):
        if(round(math.pow(a, 2) + math.pow(b, 2)) == round(math.pow(c, 2)) or round(math.pow(b, 2) + math.pow(c, 2)) == round(math.pow(a, 2)) or round(math.pow(a, 2) + math.pow(c, 2)) == round(math.pow(b, 2))):
            return "IsoscelesRight"
        else:
            return "Isosceles"
    else:
        if(round(math.pow(a, 2) + math.pow(b, 2)) == round(math.pow(c, 2)) or round(math.pow(b, 2) + math.pow(c, 2)) == round(math.pow(a, 2)) or round(math.pow(a, 2) + math.pow(c, 2)) == round(math.pow(b, 2))):
            return "ScaleneRight"
        else:
            return "Scalene"