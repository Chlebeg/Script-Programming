from lab_4.homework.deanerySystem.Lesson_class import *
import unittest

class Test_Lesson(unittest.TestCase):

    def test_lesson_creation(self):
        lesson1 = Lesson(Term(Day.MON, 8, 0, 90), "Programowanie", "Polak", 2)
        self.assertEqual(lesson1.term, Term(Day.MON, 8, 0, 90))
        self.assertEqual(lesson1.name, "Programowanie")
        self.assertEqual(lesson1.teacherName, "Polak")
        self.assertEqual(lesson1.year, 2)
        self.assertEqual(lesson1.fullTime, True)

        lesson2 = Lesson(Term(Day.FRI, 17, 0, 90), "Programowanie1", "Polak1", 2)
        self.assertEqual(lesson2.term, Term(Day.FRI, 17, 0, 90))
        self.assertEqual(lesson2.name, "Programowanie1")
        self.assertEqual(lesson2.teacherName, "Polak1")
        self.assertEqual(lesson2.year, 2)
        self.assertEqual(lesson2.fullTime, False)

    def test_earlier_day(self):
        lesson1 = Lesson(Term(Day.MON, 8, 30, 90), "Programowanie", "Polak", 2)
        lesson2 = Lesson(Term(Day.FRI, 17, 30, 120), "Programowanie1", "Polak", 3)
        lesson3 = Lesson(Term(Day.THU, 17, 30, 31), "Programowanie2", "Polak", 4)
        lesson4 = Lesson(Term(Day.SAT, 8, 5, 4), "Programowanie3", "Polak", 5)
        lesson5 = Lesson(Term(Day.SAT, 17, 0, 45), "Programowanie3", "Polak", 5)

        self.assertFalse(lesson1.earlierDay())
        self.assertFalse(lesson2.earlierDay())
        self.assertTrue(lesson3.earlierDay())
        self.assertEqual(lesson3.term, Term(Day.WED, 17, 30, 31))
        self.assertFalse(lesson4.earlierDay())
        self.assertTrue(lesson5.earlierDay())

    def test_later_day(self):
        lesson1 = Lesson(Term(Day.MON, 8, 30, 90), "Programowanie", "Polak", 2)
        lesson2 = Lesson(Term(Day.FRI, 17, 30, 120), "Programowanie1", "Polak", 3)
        lesson3 = Lesson(Term(Day.THU, 17, 30, 31), "Programowanie2", "Polak", 4)
        lesson4 = Lesson(Term(Day.SAT, 8, 5, 4), "Programowanie3", "Polak", 5)
        lesson5 = Lesson(Term(Day.SAT, 17, 0, 45), "Programowanie3", "Polak", 5)

        self.assertTrue(lesson1.laterDay())
        self.assertTrue(lesson2.laterDay())
        self.assertFalse(lesson3.laterDay())
        self.assertTrue(lesson4.laterDay())
        self.assertTrue(lesson5.laterDay())

    def test_later_time(self):
        lesson1 = Lesson(Term(Day.MON, 8, 30, 90), "Programowanie", "Polak", 2)
        lesson2 = Lesson(Term(Day.FRI, 17, 30, 120), "Programowanie1", "Polak", 3)
        lesson3 = Lesson(Term(Day.FRI, 16, 30, 31), "Programowanie2", "Polak", 4)
        lesson4 = Lesson(Term(Day.SAT, 8, 5, 4), "Programowanie3", "Polak", 5)
        lesson5 = Lesson(Term(Day.SAT, 17, 0, 45), "Programowanie3", "Polak", 5)

        self.assertTrue(lesson1.laterTime(20))
        self.assertTrue(lesson2.laterTime(30))
        self.assertFalse(lesson3.laterTime(40))
        self.assertTrue(lesson4.laterTime(360))
        self.assertFalse(lesson5.laterTime(181))

    def test_earlier_time(self):
        lesson1 = Lesson(Term(Day.MON, 8, 30, 90), "Programowanie", "Polak", 2)
        lesson2 = Lesson(Term(Day.FRI, 17, 30, 120), "Programowanie1", "Polak", 3)
        lesson3 = Lesson(Term(Day.THU, 17, 30, 31), "Programowanie2", "Polak", 4)
        lesson4 = Lesson(Term(Day.SAT, 8, 5, 4), "Programowanie3", "Polak", 5)
        lesson5 = Lesson(Term(Day.SAT, 17, 0, 45), "Programowanie3", "Polak", 5)

        self.assertFalse(lesson1.earlierTime(40))
        self.assertFalse(lesson2.earlierTime(40))
        self.assertTrue(lesson3.earlierTime(20))
        self.assertTrue(lesson4.earlierTime(5))
        self.assertTrue(lesson5.earlierTime(360))

    def test_str(self):
        lesson1 = Lesson(Term(Day.MON, 8, 30, 90), "Programowanie1", "Polak", 1)
        lesson2 = Lesson(Term(Day.FRI, 17, 30, 120), "Matematyka", "Kowal", 2)
        lesson3 = Lesson(Term(Day.THU, 17, 30, 31), "Polski", "Nill", 3)
        lesson4 = Lesson(Term(Day.SAT, 8, 5, 4), "Fizyka", "Nowak", 4)

        self.assertEqual(str(lesson1), "Programowanie1 (Poniedziałek 8:30-10:00)\nPierwszy rok studiów stacjonarnych\nProwadzący: Polak")
        self.assertEqual(str(lesson2), "Matematyka (Piątek 17:30-19:30)\nDrugi rok studiów niestacjonarnych\nProwadzący: Kowal")
        self.assertEqual(str(lesson3), "Polski (Czwartek 17:30-18:01)\nTrzeci rok studiów stacjonarnych\nProwadzący: Nill")
        self.assertEqual(str(lesson4), "Fizyka (Sobota 8:05-8:09)\nCzwarty rok studiów niestacjonarnych\nProwadzący: Nowak")

if __name__ == '__main__':
    unittest.main()
