from lab_5.homework.deanerySystem.Lesson_class import *

class Line:
    def __init__(self, start, end, isBreak, table):
        self.start = start
        self.end = end
        self.duration = (end[0] * 60 + end[1]) - (start[0] * 60 + start[1])
        self.isBreak = isBreak
        self.table = table

    def __str__(self):
        result = ""
        cell = f"{self.start[0]}:{str(self.start[1]).zfill(2)}-"
        cell += f"{self.end[0]}:{str(self.end[1]).zfill(2)}"
        result += f"{cell:^13}*"
        for day in range(0, 7):
            cell = Term(Day(day), self.start[0], self.start[1], self.duration)
            cell = self.table.get(cell)
            if self.isBreak:
                cell = "---"
            elif type(cell) == Lesson:
                cell = cell.name
            else:
                cell = ""
            result += f'{cell:^13}*'
        result += '\n'
        return result
