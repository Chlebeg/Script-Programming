import prog_2
import unittest


class Test_TestMatchCase(unittest.TestCase):
    def test_match_case_with_letter(self):
        self.assertEqual(prog_2.match_case("l", ""), "l")

    def test_match_case_with_number(self):
        self.assertEqual(prog_2.match_case("1", ""), "1")

    def test_match_case_with_blank(self):
        self.assertEqual(prog_2.match_case("", ""), "")

    def test_match_case_with_letter_and_letter_as_future_word(self):
        self.assertEqual(prog_2.match_case("l", "a"), "al")

    def test_match_case_with_letter_and_number_as_future_word(self):
        self.assertEqual(prog_2.match_case("l", "1"), "l")

    def test_match_case_with_number_and_number_as_future_word(self):
        self.assertEqual(prog_2.match_case("1", "2"), "21")

    def test_match_case_with_number_and_letter_as_future_word(self):
        self.assertEqual(prog_2.match_case("1", "l"), "1")


if __name__ == '__main__':
    unittest.main()
