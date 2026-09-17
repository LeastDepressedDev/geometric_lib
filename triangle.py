"""
Предоставляет набор функций и утилит для вычисления числовых параметров треугольника. 
"""

import unittest

def area(a: int|float, h: int|float) -> float:
    """
    Вычисляет площадь треугольника с длиной основания a и высотой h. 

    Параметры:
        a (float|int) - длина основания треугольника.
        h (float|int) - длина высоты треугольника.

    Возвращает:
        S (float) - площаль треугольника.
    """
    return a * h / 2 

def perimeter(a: int|float, b: int|float, c: int|float) -> int|float: 
    """
    Вычисляет периметр треугольника с сторонами a, b, c. Возвращаемый тип данных соответствует типу данных параметров a, b, c.

    Параметры:
        a (float|int) - сторона 1.
        b (float|int) - сторона 2.
        c (float|int) - сторона 3.

    Возвращает:
        P (float|int) - периметр треугольника.
    """
    return a + b + c


class TestsTriangle(unittest.TestCase):
    tc_test_area_calculations: list[tuple] = [
        (2, 3, 3.0),
        (1, 1, 0.5),
        (10, 10, 50.0),
        (100, 200, 10000.0),
        (1.5, 2, 1.5),
        (2.5, 4.0, 5.0),
        (4.0, 0.5, 1.0),
        (0, 5, None),
        (5, 0, None),
        (0, 0, 0), # Исключение - принимаем нулевой треугольник за фигуру площали ноль
        (-1, 5, None),
        (5, -1, None),
        (-2, -3, None),
    ]

    tc_test_area_types: list[tuple] = [
        (2, 3, float),
        (1, 1, float),
        (10, 10, float),
        (1.5, 2, float),
        (2.5, 4.0, float),
        (0, 5, type(None)),
        (5, 0, type(None)),
        (0, 0, int|float), # Исключение - принимаем нулевой треугольник за фигуру площали ноль
        (-1, 5, type(None)),
        (5, -1, type(None)),
        (-2, -3, type(None)),
    ]

    tc_test_perimeter_calculations: list[tuple] = [
        (2, 3, 4, 9),
        (1, 1, 1, 3),
        (3, 4, 5, 12),
        (10, 10, 10, 30),
        (1.5, 2, 2.5, 6.0),
        (2.5, 4.0, 3.5, 10.0),
        (100, 200, 250, 550),
        (4.0, 0.5, 3.7, 8.2),
        (0,0,0,0), # Исключение - принимаем нулевой треугольник за фигуру периметра ноль
        (0, 0, 0, None),
        (0, 5, 5, None),
        (5, 0, 5, None),
        (5, 5, 0, None),
        (100, 200, 300, None),
        (1, 2, 5, None),
        (4.0, 0.5, 1.5, None),
        (-1, 5, 5, None),
        (5, -1, 5, None),
        (5, 5, -1, None),
        (1, 1, 5, None),
    ]

    tc_test_perimeter_types: list[tuple] = [
        (2, 3, 4, int),
        (1, 1, 1, int),
        (3, 4, 5, int),
        (10, 10, 10, int),
        (1.5, 2, 2.5, float),
        (2.5, 4.0, 3.5, float),
        (0,0,0, int|float), # Исключение - принимаем нулевой треугольник за фигуру периметра ноль
        (0, 0, 0, type(None)),
        (100, 200, 300, type(None)),
        (1, 2, 5, type(None)),
        (4.0, 0.5, 1.5, type(None)),
        (-1, 5, 5, type(None)),
        (5, -1, 5, type(None)),
        (5, 5, -1, type(None)),
    ]

    def test_area_calculations(self):
        for test in TestsTriangle.tc_test_area_calculations:
            with self.subTest(test=test):
                res = area(test[0], test[1])
                self.assertEqual(res, test[2])

    def test_area_types(self):
        for test in TestsTriangle.tc_test_area_types:
            with self.subTest(test=test):
                res = area(test[0], test[1])
                self.assertIsInstance(res, test[2])

    def test_perimeter_calculations(self):
        for test in TestsTriangle.tc_test_perimeter_calculations:
            with self.subTest(test=test):
                res = perimeter(test[0], test[1], test[2])
                self.assertEqual(res, test[3])

    def test_perimeter_types(self):
        for test in TestsTriangle.tc_test_perimeter_types:
            with self.subTest(test=test):
                res = perimeter(test[0], test[1], test[2])
                self.assertIsInstance(res, test[3])
