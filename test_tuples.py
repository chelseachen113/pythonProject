from unittest import TestCase




class TestTuples(TestCase):

    def test_tuple_four_multiplied_by_nine_equals_thirty_six(self):
        tpl_factor = (4)
        tpl_factor_2 = (9)
        tpl_product = (tpl_factor * tpl_factor_2)
        self.assertEqual( 36, tpl_product )

    def test_tuple_length_of_variable_equals_three(self):
        tpl_phrase = ("blue", "red", "green")
        tpl_total = len( tpl_phrase )
        self.assertEqual( 3, tpl_total )
