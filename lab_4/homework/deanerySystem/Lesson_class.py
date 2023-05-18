from lab_4.homework.deanerySystem.Term_class import *

class Lesson:
    def __init__(self, term: Term, name: str, teacherName: str, year: int, timetable=None):
        self.__term = term
        self.__name = name
        self.__teacherName = teacherName
        self.__year = year
        self.__fullTime = self.setFullTime()
        self.timetable = None
        if timetable is not None and timetable.put(self):
            self.timetable = timetable

    def setFullTime(self):
        if Term(Day.MON, 8, 0) <= self.term < Term(Day.FRI, 17, 0):
            return True
        else:
            return False

    def earlierDay(self):
        newDay = Day((self.term.day.value - 1) % 7)
        print(newDay)
        if self.timetable is None:
            return False
        if self.timetable.can_be_transferred_to(Term(newDay,self.term.hour,self.term.minute,self.term.duration), self.fullTime):
            self.term.day = newDay
            return True
        return False

    def laterDay(self):
        newDay = Day((self.term.day.value + 1) % 7)
        if self.timetable is None:
            return False
        if self.timetable.can_be_transferred_to(Term(newDay, self.term.hour, self.term.minute, self.term.duration), self.fullTime):
            self.term.day = newDay
            return True
        return False

    def earlierTime(self, duration):
        new_term = findNewTermEarlier(self.term, duration)
        if self.timetable is None:
            return False
        if self.timetable.can_be_transferred_to(new_term, self.fullTime):
            self.term = new_term
            return True
        return False

    def laterTime(self, duration):
        new_term = findNewTermLater(self.term, duration)
        if self.timetable is None:
            return False
        if self.timetable.can_be_transferred_to(new_term, self.fullTime):
            self.term = new_term
            return True
        return False

    def __str__(self):
        if self.fullTime:
            full_time = "studiów stacjonarnych"
        else:
            full_time = "studiów niestacjonarnych"
        year = ["", "Pierwszy", "Drugi", "Trzeci", "Czwarty"]
        rok = year[self.year]
        term = str(self.term).split("[")[0][:-1]
        min = (self.term.minute + self.term.duration)%60
        hour = self.term.hour + (self.term.minute +  self.term.duration)//60
        return "{0} ({1}-{2}:{3:02d})\n{4} rok {5}\nProwadzący: {6}".format(self.name, term, hour, min, rok, full_time, self.teacherName)

    @property
    def term(self):
        return self.__term

    @term.setter
    def term(self, val):
        self.__term = val

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self.__name = val

    @property
    def teacherName(self):
        return self.__teacherName

    @teacherName.setter
    def teacherName(self, val):
        self.__teacherName = val

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, val):
        self.__year = val

    @property
    def fullTime(self):
        return self.__fullTime

    @fullTime.setter
    def fullTime(self, val):
        self.__fullTime = val

def findNewTermEarlier(term, duration):
    day = term.day
    dur = term.duration
    hours = duration // 60
    new_hours = term.hour - hours
    minutes = duration % 60
    new_minutes = term.minute - minutes
    if new_minutes < 0:
        new_minutes += 60
        new_hours -= 1
    return Term(day, new_hours, new_minutes, dur)

def findNewTermLater(term, duration):
    day = term.day
    dur = term.duration
    hours = duration // 60
    new_hours = term.hour + hours
    minutes = duration % 60
    new_minutes = term.minute + minutes
    if new_minutes >= 60:
        new_minutes -= 60
        new_hours += 1
    return Term(day, new_hours, new_minutes, dur)