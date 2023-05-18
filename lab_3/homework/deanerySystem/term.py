class Term:
    def __init__(self, Day, hour, minute, duration=90):
        self.hour = hour
        self.minute = minute
        self.duration = duration
        self.__Day = Day

    def __str__(self):
        return ("{3} {0}:{1:02d} [{2}]".format(self.hour, self.minute, self.duration, self.__Day))[4:]

    def earlierThan(self, termin):
        if self.__Day.value < termin.__Day.value:
            return True
        elif self.__Day.value == termin.__Day.value:
            if self.hour < termin.hour:
                return True
            elif self.hour == termin.hour:
                if self.minute < termin.minute:
                    return True
        return False

    def laterThan(self, termin):
        if self.__Day.value > termin.__Day.value:
            return True
        elif self.__Day.value == termin.__Day.value:
            if self.hour > termin.hour:
                return True
            elif self.hour == termin.hour:
                if self.minute > termin.minute:
                    return True
        return False

    def equals(self, termin):
        if self.__Day.value == termin.__Day.value:
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
        return Term(termin.__Day, termin.hour, termin.minute, duration)

    @property
    def day(self):
        return self.__Day

# term1 = Term(Day.MON, 8, 30)
# term3 = Term(Day.TUE, 11, 15, 90)
# term4 = term3 - term1
# print(term4)