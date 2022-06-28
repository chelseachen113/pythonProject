from unittest import TestCase


class TestBooleans(TestCase):

    # Write a test that:
    # 1. creates a boolean variable to check if 3 is greater than 4
    # 2. assert that the boolean variable is False

    def test_boolean_variable_three_is_greater_than_four_equals_false(self):
        bool_is_three_greater_than_four = 3 > 4
        self.assertEqual( False, bool_is_three_greater_than_four )
