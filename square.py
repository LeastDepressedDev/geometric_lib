"""
Предоставляет набор функций и утилит для вычисления числовых параметров квадрата. 
"""

import unittest

def area(a: float|int) -> float|int:
    """
    Вычисляет площадь квадрата с длинной ребра a. Возвращаемый тип данных соответствует типу данных параметра a.

    Параметры:
        a (float|int) - длина ребра квадрата.

    Возвращает:
        S (float|int) - площаль квадрата.
    """
    return a * a


def perimeter(a: float|int) -> float|int:
    """
    Вычисляет периметр квадрата с длинной ребра a. Возвращаемый тип данных соответствует типу данных параметра a.

    Параметры:
        a (float|int) - длина ребра квадрата.

    Возвращает:
        P (float|int) - периметр квадрата.
    """
    return 4 * a


class TestsSquare(unittest.TestCase):
    tc_test_area_calculations: list[tuple] = [
        (2, 4),
        (1, 1),
        (0, 0),
        (3, 9),
        (10, 100),
        (100, 10000),
        (0.5, 0.25),
        (1.5, 2.25),
        (2.5, 6.25),
        (4.0, 16.0),
        (-1, None),
        (-15, None)
    ]

    tc_test_area_types: list[tuple] = [
        (2, int),
        (0, int),
        (1.5, float),
        (2.5, float),
        (4.0, float),
        (-1, type(None)),
        (-15, type(None))
    ]

    tc_test_perimeter_calculations: list[tuple] = [
        (2, 8),
        (1, 4),
        (0, 0),
        (3, 12),
        (10, 40),
        (100, 400),
        (0.5, 2.0),
        (1.5, 6.0),
        (2.5, 10.0),
        (4.0, 16.0),
        (-1, None),
        (-15, None)
    ]

    tc_test_perimeter_types: list[tuple] = [
        (2, int),
        (0, int),
        (1.5, float),
        (2.5, float),
        (4.0, float),
        (-1, type(None)),
        (-15, type(None))
    ]

    def test_area_calculations(self):
        for test in TestsSquare.tc_test_area_calculations:
            with self.subTest(test=test):
                res = area(test[0])
                self.assertEqual(res, test[1])

    def test_area_types(self):
        for test in TestsSquare.tc_test_area_types:
            with self.subTest(test=test):
                res = area(test[0])
                self.assertIsInstance(res, test[1])

    def test_perimeter_calculations(self):
        for test in TestsSquare.tc_test_perimeter_calculations:
            with self.subTest(test=test):
                res = perimeter(test[0])
                self.assertEqual(res, test[1])

    def test_perimeter_types(self):
        for test in TestsSquare.tc_test_perimeter_types:
            with self.subTest(test=test):
                res = perimeter(test[0])
                self.assertIsInstance(res, test[1])
