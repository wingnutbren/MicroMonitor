import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])

print(Card.__doc__)


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                      for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

#p5
beer_card = Card('7','diamonds')
print(beer_card)

#p6
deck = FrenchDeck()
print(str(len(deck)))

print(deck[0])
print(deck[-1])

#chose randome cards
print(random.choice(deck))
print(random.choice(deck))
print(random.choice(deck))

#since __getitem__ delegates to [] the deck supports slicing
print(deck[:3])
print(deck[12::13])

#p7
print("\n\n========= it's iterable! =========")
for c in deck: #doctest: +ELLIPSIS
    print (c)

print("\n\n========= it's reverse iterable! =========")
for c in reversed(deck): #doctest: +ELLIPSIS
    print (c)

print(str(Card('7','clubs') in deck))
print(str(Card('3','sand_lizard') in deck))

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values)+suit_values[card.suit]

for card in sorted(deck,key=spades_high): #doctest: +ELLIPSIS
    print(card)


