from unittest import TestCase
import decimal


class TestMath(TestCase):

    def test_two_plus_2_equals_4(self):
        int_x = 2
        int_y = 2
        int_result = int_x + int_y
        self.assertEqual(4, int_result)

    def test_divide_8_by_1_equals_8(self):
        int_dividend = 8
        int_divisor = 1
        int_quotient = int_dividend / int_divisor
        self.assertEqual(8, int_quotient)

    def test_8_modulo_1_equals_0(self):
        int_dividend = 8
        int_divisor = 1
        int_remainder = int_dividend % int_divisor
        self.assertEqual(0, int_remainder)

    def test_8_modulo_3_equals_2(self):
        int_dividend = 8
        int_divisor = 3
        int_remainder = int_dividend % int_divisor
        self.assertEqual(2, int_remainder)

    def test_0_5_modulus_0_1_equals_0_0(self):
        flt_dividend = decimal.Decimal('0.5')
        flt_divisor = decimal.Decimal('0.1')
        flt_remainder = flt_dividend % flt_divisor
        self.assertEqual(0.0, flt_remainder)

    def test_negative59_modulus_62_equals_3(self):
        int_dividend = -59
        int_divisor = 62
        int_remainder = int_dividend % int_divisor
        self.assertEqual(3, int_remainder)

    def test_is_3_less_than_2_equal_false(self):
        is_three_less_than_two = 3 < 2
        self.assertEqual(False, is_three_less_than_two)

    # 1 Write a test that:
    # 1. multiply two integer variables
    # 2. store the result to an integer variable
    # 3. asserts the output is 45

    def test_three_multiply_two_variables_equals_forty_five(self):
        int_nine = 9
        int_five = 5
        int_total = (int_five * int_nine)
        self.assertEqual( 45, int_total )

    def test_int_dividend_divided_by_divisor_equals_thirty(self):
        int_dividend = 270
        int_divisor = 9
        int_quotient = int_dividend / int_divisor
        self.assertEqual( 30, int_quotient )