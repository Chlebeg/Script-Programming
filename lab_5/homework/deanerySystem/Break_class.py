from lab_5.homework.abstractClass.BasicTerm import *

class Break(BasicTerm):
    def __str__(self):
        return "---"

    def getTerm(self):
        return "{0}:{1:02d} [{2}]".format(self.hour, self.minute, self.duration)
