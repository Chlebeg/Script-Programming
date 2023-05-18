from deanerySystem.term import Term
from deanerySystem.day import Day

# fullTime field specs:
# TRUE - stacjonarne (MON-THU 8:00 - 20:00, FRI 8:00 - 16:59),
# FALSE - niestacjonarne (FRI 17:00 - 20:00, SAT-SUN 8:00 - 20:00)

class Lesson:
    def __init__(self, term: Term, name: str, teacherName: str, year: int):
        self.term = term
        self.name = name
        self.teacherName = teacherName
        self.year = year
        self.fullTime = setFullTime(self.term)

    def earlierDay(self):
        if self.fullTime:
            if Term(Day.TUE, 8, 0) <= self.term < Term(Day.FRI, 17, 0):
                self.term = Term(Day(self.term.day.value - 1), self.term.hour, self.term.minute, self.term.duration)
                return True
        else:
            if Term(Day.SAT, 17, 0) <= self.term <= Term(Day.SUN, 20, 0):
                self.term = Term(Day(self.term.day.value - 1), self.term.hour, self.term.minute, self.term.duration)
                return True
        return False

    def laterDay(self):
        if self.fullTime:
            if Term(Day.MON, 8, 0) <= self.term < Term(Day.THU, 17, 0):
                self.term = Term(Day(self.term.day.value + 1), self.term.hour, self.term.minute, self.term.duration)
                return True
        else:
            if Term(Day.FRI, 17, 0) <= self.term <= Term(Day.SAT, 20, 0):
                self.term = Term(Day(self.term.day.value + 1), self.term.hour, self.term.minute, self.term.duration)
                return True
        return False

    def earlierTime(self, duration):
        new_term = findNewTermEarlier(self.term, duration)
        if new_term.day.value == 4:
            if self.fullTime:
                if Term(new_term.day, 8, 0) <= new_term < Term(new_term.day, 17, 0):
                    self.term = new_term
                    return True
            else:
                if Term(new_term.day, 17, 0) <= new_term <= Term(new_term.day, 20, 0):
                    self.term = new_term
                    return True
        else:
            if Term(new_term.day, 8, 0) <= new_term <= Term(new_term.day, 20, 0):
                self.term = new_term
                return True
        return False

    def laterTime(self, duration):
        new_term = findNewTermLater(self.term, duration)
        if new_term.day.value == 4:
            if self.fullTime:
                if Term(new_term.day, 8, 0) <= new_term < Term(new_term.day, 17, 0):
                    self.term = new_term
                    return True
            else:
                if Term(new_term.day, 17, 0) <= new_term <= Term(new_term.day, 20, 0):
                    self.term = new_term
                    return True
        else:
            if Term(new_term.day, 8, 0) <= new_term <= Term(new_term.day, 20, 0):
                self.term = new_term
                return True
        return False

    def __str__(self):
        if self.fullTime:
            full_time = "studiów stacjonarnych"
        else:
            full_time = "studiów niestacjonarnych"
        if self.year == 1:
            rok = "Pierwszy"
        elif self.year == 2:
            rok = "Drugi"
        elif self.year == 3:
            rok = "Trzeci"
        else:
            rok = "Czwarty"
        term = str(self.term).split("[")[0][:-1]
        min = (self.term.minute + self.term.duration)%60
        hour = self.term.hour + (self.term.minute +  self.term.duration)//60
        return "{0} ({1}-{2}:{3:02d})\n{4} rok {5}\nProwadzący: {6}".format(self.name, term, hour, min, rok, full_time, self.teacherName)

def setFullTime(term):
    if Term(Day.MON, 8, 0) <= term < Term(Day.FRI, 17, 0):
        return True
    else:
        return False

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