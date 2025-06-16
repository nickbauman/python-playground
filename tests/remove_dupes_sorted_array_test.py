import unittest

from remove_dupes_sorted_array import remove_dupes_sorted_array


class remove_dupes_sorted_array_test(unittest.TestCase):

    def test_remove_dupes(self):
        my_list = [1, 2, 2, 3]
        deduper = remove_dupes_sorted_array()


        self.assertEqual(
            [1,2,3], deduper.rmDups(my_list)
        )



