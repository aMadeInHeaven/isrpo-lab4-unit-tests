import math
import unittest

def area(r):
    """
    Вычисляет площадь круга по длине его радиусу.

        Параметры:
                r (число): длина радиуса круга

        Возвращаемое значение:
                area_of_circle (число): площадь круга
    """

    return math.pi * r * r


def perimeter(r):
    """
    Вычисляет длину окружности по длине ее радиуса.

        Параметры:
                r (число): длина радиуса окружности

        Возвращаемое значение:
                len_of_circumference (число): длина окружности
    """

    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
    
    def test_normal_area(self):
        res = area(5)
        self.assertAlmostEqual(res, math.pi * 25)
    
    def test_float_area(self):
        res = area(2.5)
        self.assertAlmostEqual(res, math.pi * 6.25)
    
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_normal_perimeter(self):
        res = perimeter(5)
        self.assertAlmostEqual(res, 2 * math.pi * 5)
    
    def test_float_perimeter(self):
        res = perimeter(2.5)
        self.assertAlmostEqual(res, 2 * math.pi * 2.5)

    def test_negative_perimeter(self):
        res = perimeter(-4)
        self.assertAlmostEqual(res, -2 * math.pi * 4)

    def test_neg_area(self):
        res = area(-4)
        self.assertAlmostEqual(res, math.pi * 16)
