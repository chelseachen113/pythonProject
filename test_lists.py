from unittest import TestCase


class TestLists(TestCase):

    def test_is_dog_in_our_list_after_removing_doge_equals_false(self):
        lst_doge = ["doge", "house", "grass", "dog", "tree"]
        lst_doge.remove("doge")
        is_item_in_list = "doge" in lst_doge
        self.assertEqual(False, is_item_in_list)

    def test_is_boomer_in_set_after_discarding_boomer_equals_false(self):
        set_boomer = {"boomer", "boomest", "baboom"}
        set_boomer.discard("boomer")
        bool_is_item_in_set = "boomer" in set_boomer
        self.assertEqual(False, bool_is_item_in_set)

    def test_dif_set_with_two_lists_of_three_items_that_are_not_in_common_equals_three_different_items(self):
        set_egg_dog = {"egg", "dog", "set1"}
        set_big_doge = {"big", "doge", "set2"}
        set_difference = set_egg_dog.difference(set_big_doge)
        int_length_of_set_difference = len(set_difference)
        self.assertEqual(3, int_length_of_set_difference)

    def test_set_third_item_in_list_to_300(self):
        lst_numbers = [1, 2, 3, 4]
        lst_numbers[3] = 300
        value = lst_numbers[3]
        self.assertEqual(300, value)

    def test_is_doge_in_list_equals_true(self):
        bool_is_doge_in_list = False
        lst_random_values = ["7", "9", "2", 1, "doge"]
        for item in lst_random_values:
            if item == "doge":
                bool_is_doge_in_list = True
                break
        self.assertEqual(True, bool_is_doge_in_list)
