class SimpleGradebook(object):
    def __init(self):
        self.__grades = {}

    def add_student(self, name):
        self.__grades[name] = []

    def report_grade(self, name, score):
        self.__grades[name].append(score)

    def average_grade(self, name):
        grades = self.__grades[name]
        return sum(grades) / len(grades)

book = SimpleGradebook()

book.add_student('Isaak Newton')
book.report_grade('Issak Newton', 90)

book.add_student('Vitaly Gorbunow')
book.report_grade('Vitaly Gorbunov', 100)

book.report_grade('Sveta Sidoroff', 12)
