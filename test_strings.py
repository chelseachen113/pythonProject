from unittest import TestCase



class TestStrings(TestCase):

    def test_print_string_without_assertion_always_passes(self):
        quote = "We know what we are, but know not what we may be."
        print(quote)

    def test_index_string_equals_We(self):
        quote = "We know what we are, but know not what we may be."
        letters = quote[:3]
        self.assertEqual("We ", letters)
