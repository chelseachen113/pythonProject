from unittest import TestCase


def encrypt(str_value, int_shift):
    int_ascii = ord(str_value)
    int_new_ascii = int_ascii + int_shift
    str_new_value = chr(int_new_ascii)
    return str_new_value


class TestCaesarsCipher(TestCase):

    def test_a_shifted_by_1_equals_b(self):
        str_letter = "a"
        int_shift_amount = 1
        str_new_letter = encrypt(str_letter, int_shift_amount)
        self.assertEqual("b", str_new_letter)

    def test_a_shifted_by_6_equals_g(self):
        str_letter = "a"
        int_shift_amount = 6
        str_new_letter = encrypt(str_letter, int_shift_amount)
        self.assertEqual("g", str_new_letter)

    def test_g_shifted_by_negative_1_equals_f(self):
        str_letter = "g"
        int_shift_amount = -1
        str_new_letter = encrypt(str_letter, int_shift_amount)
        self.assertEqual("f", str_new_letter)
