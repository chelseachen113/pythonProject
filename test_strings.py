from unittest import TestCase


class TestStrings(TestCase):

    def test_print_string_without_assertion_always_passes(self):
        str_quote = "We know what we are, but know not what we may be."
        print(str_quote)

    def test_index_string_equals_We(self):
        str_quote = "We know what we are, but know not what we may be."
        str_letters = str_quote[:3]
        self.assertEqual("We ", str_letters)

    # 2 Write a test that:
    # 1. creates a string variable with the contents "doge"
    # 2. store the second letter to a string variable
    # 3. asserts the second string variable is "o"

    def test_access_second_letter_of_string_equals_o(self):
        str_doge = "doge"
        str_result = str_doge[1]
        self.assertEqual("o", str_result)
