import unittest
from homeworks09 import element_sum, sum_of_even_nums, unique_symbols_count


class TestElementSum(unittest.TestCase):

    def test_element_sum_raises_exception(self):
        with self.assertRaises(TypeError):
            element_sum(None)

    def test_element_sum_valid_input(self):
        self.assertEqual(element_sum(["1,2,3", "4,5,6"]), [6, 15])

    def test_element_sum_invalid_input(self):
        self.assertEqual(element_sum(["1,a,3"]), ["Не можу це зробити"])

    def test_element_sum_mixed_input(self):
        self.assertEqual(element_sum(["1,2", "g,o", "3,4"]), [3, "Не можу це зробити", 7])

    def test_element_sum_empty_list(self):
        self.assertEqual(element_sum([]), [])

class TestSumEvenNums(unittest.TestCase):

    def test_sum_of_even_nums_raises_exception(self):
        with self.assertRaises(TypeError):
            sum_of_even_nums("not a list")
    
    def test_sum_of_even_nums_negative_numbers(self):
        self.assertEqual(sum_of_even_nums([-1, -2, -3, -4]), -6)

    def test_sum_of_even_nums_valid_input(self):
        self.assertEqual(sum_of_even_nums([1, 2, 3, 4, 5, 6]), 12)

    def test_sum_of_even_nums_no_even_numbers(self):
        self.assertEqual(sum_of_even_nums([1, 3, 5]), 0)

    def test_sum_of_even_nums_empty_list(self):
        self.assertEqual(sum_of_even_nums([]), 0)

class TestUniqueSymbols(unittest.TestCase):

    def test_unique_symbols_count_raises_exception(self):
        with self.assertRaises(TypeError):
            unique_symbols_count(None)

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