from enum import Enum

class Day(Enum):
    MON = 0
    TUE = 1
    WED = 2
    THU = 3
    FRI = 4
    SAT = 5
    SUN = 6

    def difference(self, day):
        dif = day.value - self.value
        if dif >= 4:
            return dif - 7
        elif dif <= -4:
            return dif + 7
        else:
            return dif

def nthDayFrom(n, day):
    return Day((day.value + n) % 7)