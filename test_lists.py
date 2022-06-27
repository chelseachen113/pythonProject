from unittest import TestCase


# Methods can go up here


# Tests can go down here
class TestLists(TestCase):

    def test_is_dog_in_our_list_after_removing_doge_equals_false(self):
        our_list = ["doge", "house", "grass", "dog", "tree"]
        our_list.remove("doge")
        is_item_in_list = "doge" in our_list
        self.assertEqual(False, is_item_in_list)


    def test_is_boomer_in_set_after_discarding_boomer_equals_false(self):
        boomer_set = {"boomer", "boomest", "baboom"}
        boomer_set.discard("boomer")
        is_item_in_set = "boomer" in boomer_set
        self.assertEqual(False, is_item_in_set)