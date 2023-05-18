from typing import List
from lab_4.homework.deanerySystem.Lesson_class import *
from lab_4.homework.deanerySystem.Action_class import Action

class TimetableWithoutBreaks:
    """ Class containing a set of operations to manage the timetable """

    starting_hours = {(8, 0): 1, (9, 30): 2, (11, 0): 3, (12, 30): 4,
                      (14, 0): 5, (15, 30): 6, (17, 0): 7, (18, 30): 8}

    def __init__(self):
        self.lessons = []
        self.timetable = [[None for _ in range(8)] for _ in range(9)]
        self.timetable[0] = ['','Poniedzialek','Wtorek','Sroda','Czwartek','Piatek','Sobota','Niedziela']
        x,y = 8,0
        second = ""
        for i in range(1,9):
            second = str(y).zfill(2)
            time = f'{x}:{second}-'
            a,y = divmod(y+30,60)
            x += a + 1
            second = str(y).zfill(2)
            time += f'{x}:{second}'
            self.timetable[i][0] = time

    def __str__(self):
        result = ""
        column  = 14
        linebreak = ""*column + "*"*column*8 + "\n"
        for row in self.timetable:
            line = ""
            for cell in row:
                if cell == None:
                    cell = ''
                elif type(cell) == Lesson:
                    cell = cell.name
                line += f'{cell:^13}*'
            line += '\n'
            result += line + linebreak
        return result

    ##########################################################
    def can_be_transferred_to(self, term: Term, fullTime: bool) -> bool:
        """
Informs whether a lesson can be transferred to the given term

Parameters
----------
term : Term
    The term checked for the transferability
fullTime : bool
    Full-time or part-time studies

Returns
-------
bool
    **True** if the lesson can be transferred to this term
"""
        if self.busy(term):
            return False
        if fullTime:
            if Term(Day.MON, 8, 0) <= term < Term(Day.FRI, 17, 0):
                return True
        else:
            if Term(Day.FRI, 17, 0) <= term <= Term(Day.SUN, 20, 0):
                return True
        return False

##########################################################
    def busy(self, term: Term) -> bool:
        """
Informs whether the given term is busy.  Should not be confused with ``can_be_transfered_to()``
since there might be free term where the lesson cannot be transferred.

Parameters
----------
term : Term
    Checked term

Returns
-------
bool
    **True** if the term is busy
        """
        start = (term.hour, term.minute)
        if not (start in TimetableWithoutBreaks.starting_hours and term.duration == 90):
            # print("Wrong term")
            return True
        day = term.day.value + 1
        if not self.timetable[TimetableWithoutBreaks.starting_hours[start]][day]:
            return False
        return True

##########################################################
    def put(self, lesson: Lesson) -> bool:
        """
Add the given lesson to the timetable.

Parameters
----------
lesson : Lesson
    The added  lesson

Returns
-------
bool
    **True**  if the lesson was added.  The lesson cannot be placed if the timetable slot is already occupied.
        """
        if not self.can_be_transferred_to(lesson.term, lesson.fullTime):
            return False
        start = (lesson.term.hour, lesson.term.minute)
        day = lesson.term.day.value + 1
        row = TimetableWithoutBreaks.starting_hours[start]
        self.timetable[row][day] = lesson
        if lesson not in self.lessons:
            self.lessons.append((lesson, row, day))
        if not lesson.timetable:
            lesson.timetable = self
        return True

##########################################################
    def parse(self, actions: List[str]) -> List[Action]:
        """
Converts an array of strings to an array of 'Action' objects.

Parameters
----------
actions:  List[str]
    A list containing the strings: "d-", "d+", "t-" or "t+"

Returns
-------
    List[Action]
        A list containing the values:  DAY_EARLIER, DAY_LATER, TIME_EARLIER or TIME_LATER
        """
        result = []
        for action in actions:
            if action == "d-":
                result.append(Action.DAY_EARLIER)
            elif action == "d+":
                result.append(Action.DAY_LATER)
            elif action == "t-":
                result.append(Action.TIME_EARLIER)
            elif action == "t+":
                result.append(Action.TIME_LATER)
            else:
                pass
        return result

##########################################################
    def perform(self, actions: List[Action]):
        """
Transfer the lessons included in the timetable as described in the list of actions. N-th action should be sent the n-th lesson in the timetable.

Parameters
----------
actions : List[Action]
    Actions to be performed
        """
        lessons_quantity = len(self.lessons)
        for i, action in enumerate(actions):
            lesson = self.lessons[i % lessons_quantity]
            if action == Action.DAY_LATER:
                allow = lesson[0].laterDay()
                x, y = 0, 1
            elif action == Action.DAY_EARLIER:
                allow = lesson[0].earlierDay()
                x, y = 0, -1
            elif action == Action.TIME_LATER:
                allow = lesson[0].laterTime(90)
                x, y = 1, 0
            elif action == Action.TIME_EARLIER:
                allow = lesson[0].earlierTime(90)
                x, y = -1, 0
            if allow:
                self.timetable[lesson[1] + x][lesson[2] + y] = lesson[0]
                self.timetable[lesson[1]][lesson[2]] = None
                self.lessons[i % lessons_quantity] = (lesson[0], lesson[1] + x, lesson[2] + y)

##########################################################

    def get(self, term: Term):
        """
Get object (lesson) indicated by the given term.

Parameters
----------
term: Term
    Lesson date

Returns
-------
lesson: Lesson
    The lesson object or None if the term is free
        """
        start = (term.hour, term.minute)
        day = term.day.value + 1
        if not self.busy(term) or start not in TimetableWithoutBreaks.starting_hours:
            return None
        return self.timetable[TimetableWithoutBreaks.starting_hours[start]][day]
