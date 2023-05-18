import main
import unittest

class Test_TestSum(unittest.TestCase):
    def test_sum_integer_integer(self):
        self.assertEqual(main.sum(2, 2), 4)

    def test_sum_integer_float(self):
        self.assertEqual(main.sum(2, 1.5), 3.5)

    def test_sum_integer_string(self):
        self.assertEqual(main.sum(2, '2'), 4)

    def test_sum_string_string(self):
        self.assertEqual(main.sum('2.1', '2.0'), 4.1)

    def test_sum_integer_wrong_number_in_string(self):
        with self.assertRaises(ValueError): main.sum(2, 'Ala ma kota123')

    def test_sum_integer_fraction(self):
        self.assertEqual(main.sum(2, 1 / 5), 11 / 5)

    def test_sum_string_fraction(self):
        self.assertEqual(main.sum('2', 1 / 5), 2.2)

    def test_sum_fraction_fraction(self):
        self.assertEqual(main.sum(1 / 5, 1 / 2), 7 / 10)

    def test_sum_integer_complex(self):
        self.assertEqual(main.sum(2, complex(1, 2)), complex(3, 2))

    def test_sum_string_complex(self):
        self.assertEqual(main.sum('2', complex(1, 2)), complex(3, 2))

    def test_sum_complex_complex(self):
        self.assertEqual(main.sum(complex(2, 2), complex(1, 2)), complex(3, 4))

    def test_sum_integer_list(self):
        with self.assertRaises(ValueError): main.sum(1, [2, 3])

    def test_sum_integer_dict(self):
        with self.assertRaises(ValueError): main.sum(1, {1: 1, 2: 2})

    def test_sum_integer_set(self):
        with self.assertRaises(ValueError): main.sum(1, {1, 2, 3})


if __name__ == '__main__':
    unittest.main()