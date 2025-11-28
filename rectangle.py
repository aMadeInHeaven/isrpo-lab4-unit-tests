import unittest

def area(length, height):
    """
    Вычисляет площадь прямоугольника по его длине и высоте.

        Параметры:
                length (число): длина прямоугольника
                height  (число): высота прямоугольника

        Возвращаемое значение:
                area_of_rectangle (число): площадь прямоугольника
    """

    return length * height


def perimeter(length, height):
    """
    Вычисляет периметр прямоугольника по его длине и высоте.

        Параметры:
                length (число): длина прямоугольника
                height  (число): высота прямоугольника

        Возвращаемое значение:
                perimeter_of_rectangle (число): периметр прямоугольника
    """

    return 2 * (length + height)


class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    
    def test_square_area(self):
        res = area(10, 10)
        self.assertEqual(res, 100)
    
    def test_normal_area(self):
        res = area(5, 8)
        self.assertEqual(res, 40)
    
    def test_float_area(self):
        res = area(3.5, 2.5)
        self.assertAlmostEqual(res, 8.75)
    
    def test_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)
    
    def test_square_perimeter(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)
    
    def test_normal_perimeter(self):
        res = perimeter(5, 8)
        self.assertEqual(res, 26)
    
    def test_float_perimeter(self):
        res = perimeter(3.5, 2.5)
        self.assertAlmostEqual(res, 12.0)

    def test_huge_area(self):
        res = area(1000000000000000000000000000000, 10000000000000000000000000000000000000)
        self.assertAlmostEqual(res, 10000000000000000000000000000000000000000000000000000000000000000000)

