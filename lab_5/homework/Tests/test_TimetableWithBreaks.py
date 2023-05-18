from lab_5.homework.deanerySystem.TimetableWithBreakes_class import *
import unittest

less1 = Lesson(Term(Day.MON,12,10,140),"Fizyka","",1)
less2 = Lesson(Term(Day.WED,14,40,210),"Skryptowe","",1)
less3 = Lesson(Term(Day.SUN,9,30),"Kryptografia","",1)
less4 = Lesson(Term(Day.SUN,21,30),"Kryptografia","",1)
breaks = [Break(10,0,10),Break(12,0,10),Break(14,30,10),Break(18,10,10)]

class Test_TestTimetableWithBreaks(unittest.TestCase):

    def test_busy(self):
        table = TimetableWithBreakes(breaks)
        table.timetable[less1.term] = less1 
        term1 = Term(Day.MON,10,10,110)
        term2 = Term(Day.MON,12,10,140)
        term3 = Term(Day.SAT,10,10,90)
        self.assertEqual(table.busy(term1),False)
        self.assertEqual(table.busy(term2),True)
        self.assertEqual(table.busy(term3),True)
    def test_can_be_transferred(self):
        table = TimetableWithBreakes(breaks)
        table.timetable[less1.term] = less1 
        term1 = Term(Day.MON,10,10,110)
        term2 = Term(Day.MON,12,10,140)
        term3 = Term(Day.SAT,10,10,90)
        self.assertEqual(table.can_be_transferred_to(term1,1),True)
        with self.assertRaises(ValueError):
            table.can_be_transferred_to(term1,0)
        self.assertEqual(table.can_be_transferred_to(term2,1),False)
        self.assertEqual(table.can_be_transferred_to(term3,1),False)
    def test_put(self):
        table = TimetableWithBreakes(breaks)
        self.assertEqual(table.put(less1),True)
        self.assertEqual(table.put(less2),True)
        self.assertEqual(table.put(less3),False)
    def test_get(self):
        table = TimetableWithBreakes(breaks)
        table.put(less1)
        table.put(less2)
        self.assertEqual(table.get(less1.term),less1)
        self.assertEqual(table.get(less2.term),less2)
        self.assertEqual(table.get(less3.term),None)
        self.assertEqual(table.get(less4.term),None)
    def test_parse(self):
        table = TimetableWithBreakes(breaks)
        tab1 = ["d+",123,"df","t+"]
        res1 = [Action.DAY_LATER,Action.TIME_LATER]
        tab2 = ["d+","d-","t-","t+"]
        res2 = [Action.DAY_LATER,Action.DAY_EARLIER,Action.TIME_EARLIER,Action.TIME_LATER]
        with self.assertRaises(ValueError):
            table.parse(tab1)
        self.assertEqual(table.parse(tab2),res2)
#less1 = Lesson(Term(Day.MON,12,30),"Fizyka","",1)
#less2 = Lesson(Term(Day.WED,18,30),"Skryptowe","",1)
    def test_perform(self):
        breaks = [Break(10,0,10),Break(11,10,10),Break(12,20,10),Break(13,30,10)]
        table = TimetableWithBreakes(breaks)
        less1 = Lesson(Term(Day.MON,11,20,60),"Fizyka","",1, table)
        less2 = Lesson(Term(Day.WED,11,20,60),"Skryptowe","",1, table)
        print(table)
        res1 = [Action.DAY_LATER, Action.TIME_LATER, Action.DAY_LATER]
        newtable = TimetableWithBreakes(breaks)
        less3 = Lesson(Term(Day.WED,11,20,60),"Fizyka","",1, newtable)
        less4 = Lesson(Term(Day.WED,12,30,60),"Skryptowe","",1, newtable)
        table.perform(res1)
        print(table)

        self.assertEqual(str(table),str(newtable))

    def test_str(self):
        breaks = [Break(11,0,10),Break(12,0,10),Break(14,30,10),Break(17,10,10)]
        table = TimetableWithBreakes(breaks)
        less3 = Lesson(Term(Day.TUE,11,10,50),"Kryptografia","",1, table)
        less4 = Lesson(Term(Day.WED,14,40,150),"Fizyka","",1, table)
        result ="""             *Poniedzialek *   Wtorek    *    Sroda    *  Czwartek   *   Piatek    *   Sobota    *  Niedziela  *
****************************************************************************************************************
 8:00-11:00  *             *             *             *             *             *             *             *
****************************************************************************************************************
 11:00-11:10 *     ---     *     ---     *     ---     *     ---     *     ---     *     ---     *     ---     *
****************************************************************************************************************
 11:10-12:00 *             *Kryptografia *             *             *             *             *             *
****************************************************************************************************************
 12:00-12:10 *     ---     *     ---     *     ---     *     ---     *     ---     *     ---     *     ---     *
****************************************************************************************************************
 12:10-14:30 *             *             *             *             *             *             *             *
****************************************************************************************************************
 14:30-14:40 *     ---     *     ---     *     ---     *     ---     *     ---     *     ---     *     ---     *
****************************************************************************************************************
 14:40-17:10 *             *             *   Fizyka    *             *             *             *             *
****************************************************************************************************************
 17:10-17:20 *     ---     *     ---     *     ---     *     ---     *     ---     *     ---     *     ---     *
****************************************************************************************************************
 17:20-20:00 *             *             *             *             *             *             *             *
****************************************************************************************************************
"""
        self.assertEqual(str(table),result)
    

if "__main__" == __name__:
    unittest.main()
