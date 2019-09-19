class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words

    def who(self):
        return self.person

    def says(self):
        return self.words + '.'

class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'

class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'

class BablingBrook():
    def who(self):
        return 'Brook'

    def says(self):
        return 'Bable'

def who_says(obj):
    print(obj.who(), 'says',obj.says())

a1 = Quote('Vitas','hello world')
print(a1.who(), 'says', a1.says())
a2 = QuestionQuote('Sveta','Hello mip',)
print(a2.who(), 'says', a2.says())
a3= ExclamationQuote('Bogdan','Hello Moskva')
print(a3.who(),'says', a3.says())
brook = BablingBrook()
who_says(a1)
who_says(a2)
who_says(a2)
who_says(brook)
