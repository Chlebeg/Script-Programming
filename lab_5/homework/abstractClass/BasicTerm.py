class BasicTerm:
    def __init__(self, hour, minute, duration=90):
        self.__hour = hour
        self.__minute = minute
        self.__duration = duration

    def __str__(self):
        return "{3} {0}:{1:02d} [{2}]".format(self.hour, self.minute, self.duration, self.day.dayName())

    def earlierThan(self, termin):
        if self.hour < termin.hour:
            return True
        elif self.hour == termin.hour:
            if self.minute < termin.minute:
                return True
        return False

    def laterThan(self, termin):
        if self.hour > termin.hour:
            return True
        elif self.hour == termin.hour:
            if self.minute > termin.minute:
                return True
        return False

    def equals(self, termin):
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
        return BasicTerm(termin.hour, termin.minute, duration)

    def startTime(self):
        return self.hour, self.minute

    def endTime(self):
        endHour, endMinute = self.hour + (self.minute + self.duration) // 60, (self.minute + self.duration) % 60
        if endHour > 23:
            return None
        return endHour, endMinute

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, val):
        self.__hour = val

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, val):
        self.__minute = val

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, val):
        self.__duration = val