from lab_5.homework.abstractClass.BasicTimetable import *

class Timetable(BasicTimetable):
    def parse(self, actions):
        pass
    def perform(self, actions):
        pass
    def busy(self, term):
        pass
    def get(self, term: Term) -> Lesson:
        pass
    def put(self, lesson: Lesson) -> bool:
        pass

# Sprawdź, czy można tworzyć instancję klasy abstrakcyjnej — 'BasicTimetable'
try:
    timeTable = BasicTimetable()
except:
    print("Can not create abstract class instance")

# Sprawdź, czy można tworzyć instancję klasy pochodnej — 'Timetable'
timeTable = Timetable()

# Wywołujemy metodę, która NIE JEST zdefiniowana w klasie 'Timetable', a w klasie 'BasicTimetable'
timeTable.get(Term())