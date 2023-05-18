from abc import ABC, abstractmethod
from typing import List
from lab_5.homework.deanerySystem.Lesson_class import *
from lab_5.homework.deanerySystem.Action_class import Action

class BasicTimetable(ABC):
    @abstractmethod
    def busy(self, term: Term) -> bool:
        pass

##########################################################
    @abstractmethod
    def get(self, term: Term) -> Lesson:
        pass

##########################################################
    def parse(self, actions: List[str]) -> List[Action]:
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
                raise ValueError(f"Translation {action} is incorrect")
        return result

#########################################################
    def can_be_transferred_to(self, term: Term, fullTime: bool) -> bool:
        if self.busy(term):
            return False
        if fullTime:
            if Term(Day.MON, 8, 0) <= term < Term(Day.FRI, 17, 0):
                return True
        else:
            if Term(Day.FRI, 17, 0) <= term <= Term(Day.SUN, 20, 0):
                return True
        raise ValueError(f"Wrong Term!")

##########################################################
    @abstractmethod
    def perform(self, actions: List[Action]):
        pass

##########################################################
    @abstractmethod
    def put(self, lesson: Lesson) -> bool:
        pass
