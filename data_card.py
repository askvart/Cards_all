from collections import namedtuple
from random import choice

Card = namedtuple('Card',['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('VDKT')
    suits = 'kresti bubi piki chervi'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __repr__(self):
        return f'ФpенчДек {self.__class__.__name__},{self._cards}'

    def __str__(self):
        return f'{self._cards}'

if __name__=='__main__':
    beer_card = Card('7','bubi')
    deck = FrenchDeck()
    deck.qwerty = 67
    print(beer_card)
    print(deck)
    print('Первая карта:',deck[0],'Последняя карта:',deck[-1])
    print('Всего карт в колоде:',len(deck))
    print(deck.qwerty)

