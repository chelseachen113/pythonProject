from unittest import TestCase


# Methods can go up here


# Tests can go down here
class TestSandbox(TestCase):

    def test_two_equals_two(self):
        int_number = 2
        self.assertEqual(2, int_number)


    # Write a test that:
    # 1. creates a list variable with 4 items
    # 2. store the length of the list to an integer variable
    # 3. asserts the second integer variable is 4

    def test_list_one_with_four_items(self):
        my_list = ["item1", "item2", "item3", "item4"]
        length_list = len(my_list)
        self.assertEqual(4, length_list)


    # Write a test that:
    # 1. creates a boolean variable to check if 3 is greater than 4
    # 2. assert that the boolean variable is False