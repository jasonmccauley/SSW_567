from classify_triangle import classify_triangle
from screen_brand import my_brand
import pytest
import math

my_brand("HW01 -- Testing Triangle Classification")

def test_classify_triangle():
    assert classify_triangle(3, 3, 3) == "The triangle is equilateral"
    assert classify_triangle(1, 1, math.sqrt(2)) == "The triangle is isosceles and right"
    assert classify_triangle(5, 5, 8) == "The triangle is isosceles"
    assert classify_triangle(5, 8 ,5) == "The triangle is isosceles"
    assert classify_triangle(8, 5, 5) == "The triangle is isosceles"
    assert classify_triangle(3, 4, 5) == "The triangle is scalene and right"
    assert classify_triangle(5, 7, 9) == "The triangle is scalene"
    assert print(classify_triangle(3, 3, "string")) == "Please enter numbers for triangle side lengths"