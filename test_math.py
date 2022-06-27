from unittest import TestCase
import decimal

class TestMath(TestCase):

    def test_two_plus_2_equals_4(self):
        int_x = 2
        int_y = 2
        int_result = int_x + int_y
        self.assertEqual(4, int_result)

    def test_divide_8_by_1_equals_8(self):
        dividend = 8
        divisor = 1
        quotient = dividend / divisor
        self.assertEqual(8, quotient)

    def test_8_modulo_1_equals_0(self):
        dividend = 8
        divisor = 1
        remainder = dividend % divisor
        self.assertEqual(0, remainder)

    def test_8_modulo_3_equals_2(self):
        dividend = 8
        divisor = 3
        remainder = dividend % divisor
        self.assertEqual(2, remainder)

    def test_0_5_modulus_0_1_equals_0_0(self):
        dividend = decimal.Decimal('0.5')
        divisor = decimal.Decimal('0.1')
        remainder = dividend % divisor
        self.assertEqual(0.0, remainder)

    def test_negative59_modulus_62_equals_3(self):
        dividend = -59
        divisor = 62
        remainder = dividend % divisor
        self.assertEqual(3, remainder)

    def test_is_3_less_than_2_equal_false(self):
        is_three_less_than_two = 3 < 2
        self.assertEqual(False, is_three_less_than_two)