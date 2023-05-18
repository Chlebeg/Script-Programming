import unittest
from deanerySystem.term import Term
from deanerySystem.day import Day

class Test_Term(unittest.TestCase):

    def test_Term_Class(self):
        self.assertEqual(str(Term(Day.MON, 10, 45)), "MON 10:45 [90]")
        self.assertEqual(str(Term(Day.TUE, 11, 15)), "TUE 11:15 [90]")
        self.assertEqual(str(Term(Day.WED, 12, 10)), "WED 12:10 [90]")
        self.assertEqual(str(Term(Day.THU, 15, 0)), "THU 15:00 [90]")
        self.assertEqual(str(Term(Day.FRI, 5, 23)), "FRI 5:23 [90]")
        self.assertEqual(str(Term(Day.SAT, 14, 18)), "SAT 14:18 [90]")
        self.assertEqual(str(Term(Day.SUN, 12, 3)), "SUN 12:03 [90]")

    def test_earlier_than(self):
        self.assertFalse(Term(Day.TUE, 9, 45).earlierThan(Term(Day.MON, 10, 15)))
        self.assertFalse(Term(Day.SUN, 17, 00).earlierThan(Term(Day.FRI, 0, 00)))
        self.assertTrue(Term(Day.SAT, 7, 00).earlierThan(Term(Day.SUN, 2, 33)))

    def test_later_than(self):
        self.assertTrue(Term(Day.TUE, 9, 45).laterThan(Term(Day.MON, 10, 15)))
        self.assertTrue(Term(Day.SUN, 17, 00).laterThan(Term(Day.FRI, 0, 00)))
        self.assertFalse(Term(Day.SAT, 7, 00).laterThan(Term(Day.SUN, 2, 33)))

    def test_equals(self):
        self.assertTrue(Term(Day.SUN, 0, 55).equals(Term(Day.SUN, 0, 55)))
        self.assertFalse(Term(Day.SUN, 0, 55).equals(Term(Day.SUN, 0, 54)))
        self.assertFalse(Term(Day.MON, 14, 37).equals(Term(Day.TUE, 14, 37)))

if __name__ == '__main__':
    unittest.main()