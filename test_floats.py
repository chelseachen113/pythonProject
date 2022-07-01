from unittest import TestCase




class TestFloats(TestCase):


    def test_the_float_of_six_and_four_thousand_four_hundred_twenty_two_thousanths_equals_six_and_four_thousand_four_hundred_twenty_two_thousanths(self):
        flt_number = 6.4422
        flt_result = float(flt_number)
        self.assertEqual(6.4422, flt_result)

    def test_the_float_of_four_sixths_equals_four_sixths(self):
        flt_number = 4/6
        flt_result = float(flt_number)
        self.assertEqual(4/6, flt_result)
