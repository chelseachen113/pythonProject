from unittest import TestCase


# Methods can go up here


# Tests can go down here
class TestSandbox(TestCase):

    def test_two_equals_two(self):
        int_number = 2
        self.assertEqual(2, int_number)


    def test_int_dividend_divided_by_divisor_equals_thirty(self):
        int_dividend = 270
        int_divisor = 9
        int_quotient = int_dividend / int_divisor
        self.assertEqual(30, int_quotient)

    def test_str_length_of_quote_equals_7(self):
        str_quote = "python"
        str_total = len(str_quote)
        self.assertEqual(6, str_total)

