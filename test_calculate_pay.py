from unittest import TestCase
from calculate_pay import calculate_pay


class TestCalculate(TestCase):
    def test_20_hours_10_wages(self):
        expected = 200.0
        actual = calculate_pay(20, 10)
        self.assertEqual(expected, actual)

    def test_55_hours_10_wages(self):
        expected = 700.0
        actual = calculate_pay(55, 10)
        self.assertEqual(expected, actual)

    def test_0_hours_10_wages(self):
        expected = 0.0
        actual = calculate_pay(0, 10)
        self.assertEqual(expected, actual)
