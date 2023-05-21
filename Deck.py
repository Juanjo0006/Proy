import Cartas as C
import random

SUITS = ['Corazones', 'Diamantes', 'Picas', 'Tréboles']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

class Deck:
    def __init__(self):
        self.deck = []
        for palo in PALOS:
            for suits in SUITS:
                for rank in RANKS:
                    self.deck.append(C.Carta(suits, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card