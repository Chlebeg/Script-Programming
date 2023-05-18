from lab_5.homework.abstractClass.BasicTerm import BasicTerm
from lab_5.homework.deanerySystem.Day_class import Day

class Term(BasicTerm):
    def __init__(self, day, hour, minute, duration=90):
        super().__init__(hour, minute, duration)
        self.__day = day

    def __str__(self):
        return "{3} {0}:{1:02d} [{2}]".format(self.hour, self.minute, self.duration, self.day.dayName())

    def earlierThan(self, termin):
        if self.__day.value < termin.__day.value:
            return True
        elif self.__day.value == termin.__day.value:
            if self.hour < termin.hour:
                return True
            elif self.hour == termin.hour:
                if self.minute < termin.minute:
                    return True
        return False

    def laterThan(self, termin):
        if self.__day.value > termin.__day.value:
            return True
        elif self.__day.value == termin.__day.value:
            if self.hour > termin.hour:
                return True
            elif self.hour == termin.hour:
                if self.minute > termin.minute:
                    return True
        return False

    def equals(self, termin):
        if self.__day.value == termin.__day.value:
            if self.hour == termin.hour:
                if self.minute == termin.minute:
                    return True
        return False

    def __lt__(self, termin):
        return self.earlierThan(termin)

    def __le__(self, termin):
        if self.earlierThan(termin) or self.equals(termin):
            return True
        return False

    def __gt__(self, termin):
        return self.laterThan(termin)

    def __ge__(self, termin):
        if self.laterThan(termin) or self.equals(termin):
            return True
        return False

    def __eq__(self, termin):
        return self.equals(termin)

    def __sub__(self, termin):
        duration = (self.hour * 60 + self.minute + self.duration) + 1440 - (termin.hour * 60 + termin.minute + termin.duration)
        return Term(termin.__day, termin.hour, termin.minute, duration)

    def __hash__(self):
        return hash(60*self.hour + self.minute + 24*60*self.__day.value)

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, val):
        if type(val) != Day:
            print("Wrong type")
            return 0
        self.__day = val