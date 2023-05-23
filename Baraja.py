# Crear una baraja de cartas
import random

def crear_baraja():
    baraja = []
    palos = ['Corazones', 'Diamantes', 'Picas', 'Tréboles']
    valores = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    for palo in palos:
        for valor in valores:
            baraja.append((valor, palo))
    return baraja
    
# Repartir una carta de la baraja a una mano
def repartir_carta(baraja, mano):
    carta = random.choice(baraja)
    baraja.remove(carta)
    mano.append(carta)