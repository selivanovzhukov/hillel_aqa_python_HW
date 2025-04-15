import unittest
from homeworks import element_sum, sum_of_even_nums, unique_symbols_count


class TestHomework(unittest.TestCase):

    def test_element_sum_valid_input(self):
        element_sum(["1,2,3", "4,5,6"])

    def test_element_sum_invalid_input(self):
        element_sum(["1,a,3"])

    def test_element_sum_empty_list(self):
        element_sum([])

    def test_sum_of_even_nums_valid_input(self):
        self.assertEqual(sum_of_even_nums([1, 2, 3, 4, 5, 6]), 12)

    def test_sum_of_even_nums_no_even_numbers(self):
        self.assertEqual(sum_of_even_nums([1, 3, 5]), 0)

    def test_sum_of_even_nums_empty_list(self):
        self.assertEqual(sum_of_even_nums([]), 0)

    def test_unique_symbols_count_true(self):
        self.assertTrue(unique_symbols_count(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']))

    def test_unique_symbols_count_false(self):
        self.assertFalse(unique_symbols_count(['a', 'b', 'c', 'd']))

    def test_unique_symbols_count_duplicate_symbols(self):
        self.assertFalse(unique_symbols_count(['a', 'a', 'a', 'a', 'a', 'b', 'c', 'd', 'e', 'f']))

    def test_unique_symbols_count_empty_list(self):
        self.assertFalse(unique_symbols_count([]))

if __name__ == '__main__':
    unittest.main()