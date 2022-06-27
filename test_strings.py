from unittest import TestCase


class TestStrings(TestCase):

    def test_print_string_without_assertion_always_passes(self):
        str_quote = "We know what we are, but know not what we may be."
        print(str_quote)

    def test_index_string_equals_We(self):
        str_quote = "We know what we are, but know not what we may be."
        str_letters = str_quote[:3]
        self.assertEqual("We ", str_letters)
