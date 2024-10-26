import unittest
import math
from classify_triangle import classify_triangle

class TestClassifyTriangle(unittest.TestCase):
    """ test suite for the classify_triangle program """
    def test_equilateral(self):
        """ test for equilateral triangle, all sides equal """
        result = classify_triangle(3, 3, 3)
        self.assertEqual(result, "The triangle is equilateral")
    
    def test_isosceles_right(self):
        """ test for isosceles right triangle, two sides equal and right angle """
        result = classify_triangle(1, 1, math.sqrt(2))
        self.assertEqual(result, "The triangle is isosceles and right")
    
    def test_isosceles(self):
        """ test for isosceles triangle, two sides equal only """
        result1 = classify_triangle(5, 5, 8)
        result2 = classify_triangle(5, 8 ,5)
        result3 = classify_triangle(8, 5, 5)
        self.assertEqual(result1, "The triangle is isosceles")
        self.assertEqual(result2, "The triangle is isosceles")
        self.assertEqual(result3, "The triangle is isosceles")

    def test_scalene_right(self):
        """ test for scaelene right triangle, all sides are different and right angle """
        result = classify_triangle(3, 4, 5)
        self.assertEqual(result, "The triangle is scalene and right")

    def test_scalene(self):
        """ test for scalene triangle, all sides different only """
        result = classify_triangle(5, 7, 9)
        self.assertEqual(result, "The triangle is scalene")

    def test_check_inputs_type(self):
        """ test for invalid input with string """
        result = classify_triangle(3, 4, "string")
        self.assertEqual(result, "Please enter numbers for triangle side lengths")

    def test_check_inputs_negative(self):
        """ test for invalid input with negative side lengths """
        result = classify_triangle(-3, 4, 5)
        self.assertEqual(result, "Triangle side lengths cannot be negative")

    def test_check_inputs_side_lengths(self):
        """ test for invalid input that does not form a possible triangle """
        result = classify_triangle(4, 4, 27)
        self.assertEqual(result, "The sum of two side lengths of a triangle must be greater than the third side length")

if __name__ == "__main__":
    unittest.main()
