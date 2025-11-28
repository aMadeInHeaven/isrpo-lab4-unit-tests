import unittest

def area(a, height):
    """
    Вычисляет площадь треугольника по длине его основанию и высоте,
    проведенной к этому основанию.

        Параметры:
                a (число): длина основания треугольника
                height (число): длина высоты трегольника

        Возвращаемое значение:
                area_of_triangle (число): площадь треугольника
    """

    return (a * height) / 2


def perimeter(a, b, c):
    """
    Вычисляет периметр треугольника по длинам трех его сторон.

        Параметры:
                a (число): длина первой стороны треугольника
                b (число): длина второй стороны треугольника
                c (число): длина третьей стороны треугольника

        Возвращаемое значение:
                perimeter_of_triangle (число): периметр треугольника
    """

    return a + b + c


class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    
    def test_normal_area(self):
        res = area(6, 4)
        self.assertEqual(res, 12)
    
    def test_float_area(self):
        res = area(5.5, 3.2)
        self.assertAlmostEqual(res, 8.8)
    
    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)
    
    def test_normal_perimeter(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)
    
    def test_float_perimeter(self):
        res = perimeter(2.5, 3.5, 4.5)
        self.assertAlmostEqual(res, 10.5)
