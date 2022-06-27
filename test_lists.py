from unittest import TestCase


# Methods can go up here


# Tests can go down here
class TestLists(TestCase):

    def test_is_dog_in_our_list_after_removing_doge_equals_false(self):
        doge_list = ["doge", "house", "grass", "dog", "tree"]
        doge_list.remove("doge")
        is_item_in_list = "doge" in doge_list
        self.assertEqual(False, is_item_in_list)


    def test_is_boomer_in_set_after_discarding_boomer_equals_false(self):
        boomer_set = {"boomer", "boomest", "baboom"}
        boomer_set.discard("boomer")
        is_item_in_set = "boomer" in boomer_set
        self.assertEqual(False, is_item_in_set)
        
    def test_dif_set_with_two_lists_of_three_items_that_are_not_in_common_equals_three_different_items(self):
        egg_dog_set = {"egg", "dog", "set1"}
        big_doge_set = {"big", "doge", "set2"}
        dif_set = egg_dog_set.difference(big_doge_set)
        total_items = len(dif_set)
        self.assertEqual(3, total_items)