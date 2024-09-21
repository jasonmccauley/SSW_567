import math

def classify_triangle(side1, side2, side3):
    try:
        check_inputs(side1, side2, side3)
        right = check_right(side1, side2, side3)

        if (side1 == side2 == side3):
            return "The triangle is equilateral"
        elif ((side1 == side2) or (side2 == side3) or (side1 == side3)):
            if (right):
                return "The triangle is isosceles and right"
            else:
                return "The triangle is isosceles"
        else:
            if (right):
                return "The triangle is scalene and right"
            else:
                return "The triangle is scalene"
    except(ValueError, TypeError) as e:
        return e

def check_inputs(num1, num2, num3):
    if (not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)) or not isinstance(num3, (int, float))):
        raise TypeError("Please enter numbers for triangle side lengths")
    
    if (num1 < 0 or num2 < 0 or num3 < 0):
        raise ValueError("Triangle side lengths cannot be negative")
    
    if ((num1 + num2 < num3) or (num2 + num3 < num1) or (num1 + num3 < num2)):
        raise ValueError("The sum of two side lengths of a triangle must be greater than the third side length")
    
def check_right(num1, num2, num3):
    if ((round(math.pow(num1, 2)) + round(math.pow(num2, 2)) == round(math.pow(num3, 2))) or (round(math.pow(num2, 2)) + round(math.pow(num3, 2)) == round(math.pow(num1, 2))) or (round(math.pow(num1, 2)) + round(math.pow(num3, 2)) == round(math.pow(num2, 2)))):
        return True
    else:
        return False
