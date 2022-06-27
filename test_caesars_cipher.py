from unittest import TestCase


def encrypt(text, shift):
    ascii_int = ord(text)
    new_ascii = ascii_int + shift
    new_text = chr(new_ascii)
    return new_text


class TestCaesarsCipher(TestCase):

    def test_a_shifted_by_1_equals_b(self):
        letter = "a"
        shift_amount = 1
        new_letter = encrypt(letter, shift_amount)
        self.assertEqual("b", new_letter)

    def test_a_shifted_by_6_equals_g(self):
        letter = "a"
        shift_amount = 6
        new_letter = encrypt(letter, shift_amount)
        self.assertEqual("g", new_letter)

    def test_g_shifted_by_negative_1_equals_f(self):
        letter = "g"
        shift_amount = -1
        new_letter = encrypt(letter, shift_amount)
        self.assertEqual("f", new_letter)
