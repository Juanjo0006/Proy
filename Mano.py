import Deck as Deck
import Cartas as C
import random


class mano:
    def __init__(self):
        self.mano_oculta = None
        self.mano_visible = None

    def jugar(self, baraja: Deck):
        self.mano_oculta = mano(baraja.repartir(1))
        self.mano_visible = mano(baraja.repartir(1))

    def revelar_carta_oculta(self):
        self.mano_visible.cartas = self.mano_oculta.cartas + self.mano_visible.cartas
        self.mano_oculta = None