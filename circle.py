"""
Предоставляет набор функций и утилит для вычисления числовых параметров круга/окружности. 
"""

import math
import unittest


def area(r: float) -> float:
    """
    Вычисляет площадь круга радиусом r. 

    Параметры:
        r (float) - радиус круга.

    Возвращает:
        S (float) - площаль круга.
    """
    return math.pi * r * r


def perimeter(r: float) -> float:
    """
    Вычисляет периметр круга/длину окружности радиусом r. 

    Параметры:
        r (float) - радиус круга/окружности.

    Возвращает:
        P (float) - периметр круга/длина окружности.
    """
    return 2 * math.pi * r


class TestsCircle(unittest.TestCase):
    tc_test_perimeter_calculations: list[tuple] = [
        (17, 106.76),
        (0, 0),
        (100, 628.0),
        (1, 6.28),
        (-1, None),
        (-194141, None),
        (-414.4141, None)
    ]

    tc_test_perimeter_types: list[tuple] = [
        (2, float),
        (54, float),
        (10000000, float),
        (1, float),
        (0, float),
        (-1, type(None)),
        (-5.1, type(None)),
        (1.5, float),
        (17.3333333, float)
    ]

    tc_test_area_calculations: list[tuple] = [
        (2, 12.56),
        (7, 153.86),
        (188, 110980.16),
        (10000, 314000000.0),
        (-1, None),
        (-194141, None),
        (-414.4141, None)
    ]

    tc_test_area_types: list[tuple] = [
        (2, float),
        (54, float),
        (10000000, float),
        (1, float),
        (0, float),
        (-1, type(None)),
        (-5.1, type(None)),
        (1.5, float),
        (17.3333333, float)
    ]


    def test_perimeter_calculations(self):
        for test in TestsCircle.tc_test_perimeter_calculations:
            res = perimeter(test[0])
            self.assertEqual(res, test[1])

    def test_perimeter_types(self):
        for test in TestsCircle.tc_test_perimeter_types:
            res = perimeter(test[0])
            self.assertIsInstance(res, test[1])

    def test_area_calculations(self):
        for test in TestsCircle.tc_test_area_calculations:
            res = area(test[0])
            self.assertEqual(res, test[1])

    def test_area_types(self):
        for test in TestsCircle.tc_test_area_types:
            res = area(test[0])
            self.assertIsInstance(res, test[1])

