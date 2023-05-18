import unittest
from lab_4.homework.deanerySystem.TimetableWithoutBreaks_class import *

less1 = Lesson(Term(Day.MON, 12, 30), "Fizyka", "", 1)
less2 = Lesson(Term(Day.WED, 18, 30), "Skryptowe", "", 1)
less3 = Lesson(Term(Day.SUN, 9, 30), "Kryptografia", "", 1)
less4 = Lesson(Term(Day.SUN, 21, 30), "Kryptografia", "", 1)


class Test_TestTable(unittest.TestCase):

    def test_busy(self):
        table = TimetableWithoutBreaks()
        table.timetable[4][1] = less1
        term1 = Term(Day.MON, 11, 0)
        term2 = Term(Day.MON, 12, 30)
        term3 = Term(Day.SAT, 11, 10)
        self.assertEqual(table.busy(term1), False)
        self.assertEqual(table.busy(term2), True)
        self.assertEqual(table.busy(term3), True)

    def test_can_be_transferred(self):
        table = TimetableWithoutBreaks()
        table.timetable[4][1] = less1
        term1 = Term(Day.MON, 11, 0)
        term2 = Term(Day.MON, 12, 30)
        term3 = Term(Day.SAT, 11, 10)
        self.assertEqual(table.can_be_transferred_to(term1, 1), True)
        self.assertEqual(table.can_be_transferred_to(term1, 0), False)
        self.assertEqual(table.can_be_transferred_to(term2, 1), False)
        self.assertEqual(table.can_be_transferred_to(term3, 1), False)

    def test_put(self):
        table = TimetableWithoutBreaks()
        self.assertEqual(table.put(less1), True)
        self.assertEqual(table.put(less2), True)
        self.assertEqual(table.put(less3), True)

    def test_get(self):
        table = TimetableWithoutBreaks()
        table.put(less1)
        table.put(less2)
        table.put(less3)
        print(table)
        print(table.get(less1.term))
        print(less1)
        self.assertEqual(table.get(less1.term), less1)
        self.assertEqual(table.get(less2.term), less2)
        self.assertEqual(table.get(less3.term), less3)
        self.assertEqual(table.get(less4.term), None)

    def test_parse(self):
        table = TimetableWithoutBreaks()
        tab1 = ["d+", 123, "df", "t+"]
        res1 = [Action.DAY_LATER, Action.TIME_LATER]
        tab2 = ["d+", "d-", "df", "t-", "t+"]
        res2 = [Action.DAY_LATER, Action.DAY_EARLIER, Action.TIME_EARLIER, Action.TIME_LATER]
        self.assertEqual(table.parse(tab1), res1)
        self.assertEqual(table.parse(tab2), res2)

    # less1 = Lesson(Term(Day.MON,12,30),"Fizyka","",1)
    # less2 = Lesson(Term(Day.WED,18,30),"Skryptowe","",1)
    def test_perform(self):
        table = TimetableWithoutBreaks()
        less1 = Lesson(Term(Day.MON, 12, 30), "Fizyka", "", 1, table)
        less2 = Lesson(Term(Day.WED, 17, 00), "Skryptowe", "", 1, table)
        res1 = [Action.DAY_LATER, Action.TIME_LATER, Action.DAY_LATER, Action.TIME_EARLIER]
        newtable = TimetableWithoutBreaks()
        less3 = Lesson(Term(Day.WED, 12, 30), "Fizyka", "", 1, newtable)
        less4 = Lesson(Term(Day.WED, 17, 00), "Skryptowe", "", 1, newtable)
        table.perform(res1)
        self.assertEqual(str(table), str(newtable))

    def test_str(self):
        table = TimetableWithoutBreaks()
        less1 = Lesson(Term(Day.MON, 12, 30), "Fizyka", "", 1, table)
        less2 = Lesson(Term(Day.WED, 18, 30), "Skryptowe", "", 1, table)
        less3 = Lesson(Term(Day.SUN, 9, 30), "Kryptografia", "", 1, table)
        result = """             *Poniedzialek *   Wtorek    *    Sroda    *  Czwartek   *   Piatek    *   Sobota    *  Niedziela  *
****************************************************************************************************************
  8:00-9:30  *             *             *             *             *             *             *             *
****************************************************************************************************************
 9:30-11:00  *             *             *             *             *             *             *Kryptografia *
****************************************************************************************************************
 11:00-12:30 *             *             *             *             *             *             *             *
****************************************************************************************************************
 12:30-14:00 *   Fizyka    *             *             *             *             *             *             *
****************************************************************************************************************
 14:00-15:30 *             *             *             *             *             *             *             *
****************************************************************************************************************
 15:30-17:00 *             *             *             *             *             *             *             *
****************************************************************************************************************
 17:00-18:30 *             *             *             *             *             *             *             *
****************************************************************************************************************
 18:30-20:00 *             *             *  Skryptowe  *             *             *             *             *
****************************************************************************************************************
"""
        self.assertEqual(str(table), result)


if "__main__" == __name__:
    unittest.main()