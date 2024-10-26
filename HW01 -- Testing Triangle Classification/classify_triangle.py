import math

def classify_triangle(side1, side2, side3):
    """ main function to classify the triangle according to the inputted sidelengths """
    check = check_inputs(side1, side2, side3)
    if isinstance(check, str):
        return check
    right = check_right(side1, side2, side3)

    if side1 == side2 == side3:
        return "The triangle is equilateral"
    if (side1 == side2) or (side2 == side3) or (side1 == side3):
        if right:
            return "The triangle is isosceles and right"
        return "The triangle is isosceles"
    if right:
        return "The triangle is scalene and right"
    return "The triangle is scalene"

def check_inputs(num1, num2, num3):
    """ helper function to check if inputted side lengths are proper type, non-negative, and form a valid triangle """
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)) or not isinstance(num3, (int, float)):
        return "Please enter numbers for triangle side lengths"
    if num1 < 0 or num2 < 0 or num3 < 0:
        return "Triangle side lengths cannot be negative"
    if (num1 + num2 < num3) or (num2 + num3 < num1) or (num1 + num3 < num2):
        return "The sum of two side lengths of a triangle must be greater than the third side length"
    
def check_right(num1, num2, num3):
    """ helper function for checking if the inputted triangle is right """
    return ((round(math.pow(num1, 2)) + round(math.pow(num2, 2)) == round(math.pow(num3, 2))) or (round(math.pow(num2, 2)) + round(math.pow(num3, 2)) == round(math.pow(num1, 2))) or (round(math.pow(num1, 2)) + round(math.pow(num3, 2)) == round(math.pow(num2, 2))))
