from unittest import TestCase


# Methods can go up here


# Tests can go down here
class TestSandbox(TestCase):

    def test_two_equals_two(self):
        int_number = 2
        self.assertEqual(2, int_number)

    # 1 Write a test that:
    # 1. multiply two integer variables
    # 2. store the result to an integer variable
    # 3. asserts the output is 45

    def test_three_doge(self):
        int_variable = 9
        int_variable2 = 5
        total=(int_variable * int_variable2)
        self.assertEqual(45, total)


    # 2 Write a test that:
    # 1. creates a string variable with the contents "doge"
    # 2. store the second letter to a string variable
    # 3. asserts the second string variable is "o"






    # 3 Write a test that:
    # 1. creates a list variable with 4 items
    # 2. store the length of the list to an integer variable
    # 3. asserts the second integer variable is 4


