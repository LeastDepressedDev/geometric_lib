"""
Предоставляет набор функций и утилит для вычисления числовых параметров прямоугольника. 
"""

import unittest

def area(a: int|float, b: int|float) -> int|float:
    """
    Вычисляет площадь прямоугольника, стороны которого a, b. Возвращаемый тип данных соответствует типу данных параметров a, b.

    Параметры:
        a (float|int) - сторона прямоугольника.
        b (float|int) - другая сторона прямоугольника.

    Возвращает:
        S (float|int) - площаль прямоугольника.
    """
    return a * b 

def perimeter(a: int|float, b: int|float) -> int|float: 
    """
    Вычисляет периметр прямоугольника, стороны которого a, b. Возвращаемый тип данных соответствует типу данных параметров a, b.

    Параметры:
        a (float|int) - сторона прямоугольника.
        b (float|int) - другая сторона прямоугольника.

    Возвращает:
        P (float|int) - периметр прямоугльника.
    """
    return 2*(a + b)


class TestsRectangle(unittest.TestCase):
    tc_test_area_calculations: list[tuple] = [
        (2, 3, 6),
        (0, 5, 0),
        (5, 0, 0),
        (0, 0, 0),
        (1, 1, 1),
        (10, 10, 100),
        (1.5, 2, 3.0),
        (2.5, 4.0, 10.0),
        (100, 200, 20000),
        (-1, 5, None),
        (5, -1, None),
        (-2, -3, None),
    ]

    tc_test_area_types: list[tuple] = [
        (2, 3, int),
        (1.5, 2, float),
        (2, 1.5, float),
        (1.5, 2.5, float),
        (0, 0, int),
        (-1, 5, type(None)),
        (5, -1, type(None)),
        (-2, -3, type(None)),
    ]

    tc_test_perimeter_calculations: list[tuple] = [
        (2, 3, 10),
        (0, 5, 10),
        (5, 0, 10),
        (0, 0, 0),
        (1, 1, 4),
        (10, 10, 40),
        (1.5, 2, 7.0),
        (2.5, 4.0, 13.0),
        (100, 200, 600),
        (-1, 5, None),
        (5, -1, None),
        (-2, -3, None),
    ]

    tc_test_perimeter_types: list[tuple] = [
        (2, 3, int),
        (1.5, 2, float),
        (2, 1.5, float),
        (1.5, 2.5, float),
        (0, 0, int),
        (-1, 5, type(None)),
        (5, -1, type(None)),
        (-2, -3, type(None))
    ]

    def test_area_calculations(self):
        for test in TestsRectangle.tc_test_area_calculations:
            with self.subTest(test=test):
                res = area(test[0], test[1])
                self.assertEqual(res, test[2])

    def test_area_types(self):
        for test in TestsRectangle.tc_test_area_types:
            with self.subTest(test):
                res = area(test[0], test[1])
                self.assertIsInstance(res, test[2])

    def test_perimeter_calculations(self):
        for test in TestsRectangle.tc_test_perimeter_calculations:
            with self.subTest(test=test):
                res = perimeter(test[0], test[1])
                self.assertEqual(res, test[2])

    def test_perimeter_types(self):
        for test in TestsRectangle.tc_test_perimeter_types:
            with self.subTest(test=test):
                res = perimeter(test[0], test[1])
                self.assertIsInstance(res, test[2])
