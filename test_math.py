from unittest import TestCase


class TestMath(TestCase):

    # test naming format
    # def test_scenario_equals_value
    #   self.assertEqual(expected_value, actual_value)

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

    def test_modulo_with_even_number_return(self):
        dividend = 8
        divisor = 1
        remainder = dividend % divisor
        self.assertEqual(0, remainder)
