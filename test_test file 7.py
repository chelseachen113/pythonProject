from unittest import TestCase


class Test( TestCase ):
    def test_print_hi(self):
        self.assertEqual(print_hi(0), 0)
        self.assertEqual( print_hi(1), 1)
        self.assertEqual( print_hi(2), 1)
        self.assertEqual( print_hi(3), 2)
        self.assertEqual( print_hi(4), 3)
        self.assertEqual( print_hi(5), 5)

class Test( TestCase ):
    def test_print_hi(self):
        self.fail()

    def test_get_n_digit(self):
        self.fail()

