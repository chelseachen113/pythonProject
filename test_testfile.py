from unittest import TestCase


class Test( TestCase ):
    def test_print_hi2(self):
        self.assertEqual( print_hi(0), 0)

def print_hi(this_number):
        print('hello')
        return 0
class Test2( TestCase ):
    def test_print_hi(self):
        self.fail()

    def test_get_n_digit(self):
        self.fail()
