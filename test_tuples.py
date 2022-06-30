from unittest import TestCase




class TestTuples(TestCase):

    def test_tuple_four_multiplied_by_nine_equals_thirty_six(self):
        tpl_numbers = (4, 7, 8, 1)
        int_total = len(tpl_numbers)
        self.assertEqual(4, int_total)

    def test_tuple_length_of_variable_equals_three(self):
        tpl_phrase = ("blue", "red", "green")
        int_total = len( tpl_phrase )
        self.assertEqual( 3, int_total )
