import unittest

def area(a):
    """
    Вычисляет площадь квадрата по длине его стороны.

        Параметры:
                a (число): длина стороны квадрата

        Возвращаемое значение:
                area_of_square (число): площадь квадрата
    """

    return a * a


def perimeter(a):
    """
    Вычисляет периметр квадрата по длине его стороны.

        Параметры:
                a (число): длина стороны квадрата

        Возвращаемое значение:
                perimeter_of_square (число): периметр квадрата
    """

    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
    
    def test_normal_area(self):
        res = area(5)
        self.assertEqual(res, 25)
    
    def test_float_area(self):
        res = area(3.5)
        self.assertAlmostEqual(res, 12.25)
    
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_normal_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 20)
    
    def test_float_perimeter(self):
        res = perimeter(3.5)
        self.assertAlmostEqual(res, 14.0)
