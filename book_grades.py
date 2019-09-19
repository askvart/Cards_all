class Book:
    def __init__(self):
        self.grades = {}

    def add_student(self, name):
        self.grades[name]= []

    def report_grade(self, name, score):
        self.grades[name].append(score)

    def average(self, name):
        grandes = self.grades[name]
        return sum(grandes)/len(grandes)

book = Book()
book.add_student('abba')
book.report_grade('abba',90)
print(book.average('abba'))

