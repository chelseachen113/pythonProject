from unittest import TestCase


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


    def test_set_third_item_in_list_to_300(self):
        int_list = [1,2,3,4]
        int_list[3] = 300
        value = int_list[3]
        self.assertEqual(300, value)

    def test_is_doge_in_list_equals_true(self):
        is_doge_in_list = False
        my_list = ["7", "9", "2", 1, "doge"]
        for n in my_list:
            if n == "doge":
                is_doge_in_list = True
                break
        self.assertEqual(True, is_doge_in_list)