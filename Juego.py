#Juego.py
import Deck as Deck
import Cartas as C
import Mano as M
import random

class game:
    def __init__(self, playernames):
        self.winer = ""
        
        deck = D.Deck()
        deck.shuffle = ()

        playerhanslist = []
        for player in playernames: 
            
            playerhand = M.mano(player)
            playerhand.add_new_card(deck.deal())
            playerhand.add_new_card(deck.deal())
            playerhanslist.append(playerhand)

        dealerhand= M,mano("Dealer")
        playerhand.add_new_card(deck.deal())
        playerhand.add_new_card(deck.deal())
        
        
    def calcular_puntos(self) -> int:
        puntos = 0
        tiene_as = False
        for carta in self.cartas:
            valor = carta[1]
            if valor.isnumeric():
                puntos += int(valor)
            elif valor in ('Jota', 'Reina', 'Rey'):
                puntos += 10
            else:
                tiene_as = True
                puntos += 1

        if tiene_as and puntos <= 11:
            puntos += 10

        return puntos

    def agregar_carta(self, carta: tuple):
        self.cartas.append(carta)

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = None

    def jugar(self, baraja: Deck):
        self.mano = Mano(baraja.repartir(2))

    def pedir_carta(self, baraja: Deck):
        self.mano.agregar_carta(baraja.repartir(1)[0])



class Juego:
    def __init__(self, jugador, dealer, baraja):
        self.jugador = jugador
        self.dealer = dealer
        self.baraja = baraja

    def jugar(self):
        self.jugador.jugar(self.baraja)
        self.dealer.jugar(self.baraja)

        print(f"\nEl dealer muestra una carta: {self.dealer.mano_visible.cartas[0]}")
        print(f"Tus cartas: {self.jugador.mano.cartas} - ({self.jugador.mano.calcular_puntos()} puntos)")

        if self.jugador.mano.calcular_puntos() == 21:
            print("¡Blackjack! ¡Ganaste!")
            return 'ganado'
        
        while True:
            opcion = input("¿Quieres otra carta? (S/N): ")
            if opcion.lower() == 's':
                self.jugador.pedir_carta(self.baraja)
                print(f"Tu carta: {self.jugador.mano.cartas[-1]}")
                
                puntos = self.jugador.mano.calcular_puntos()
                print(f"Tus cartas: {self.jugador.mano.cartas} - ({puntos} puntos)")

                if puntos > 21:
                    print("Te pasaste de 21. Perdiste.")
                    return 'perdido'
            else:
                break

        dealer_puntos = self.dealer.mano_visible.calcular_puntos()
        print(f"Las cartas del dealer son: {self.dealer.mano_visible.cartas} - ({dealer_puntos} puntos)")

        while dealer_puntos < 17:
            print("El dealer toma otra carta.")
            self.dealer.mano_visible.agregar_carta(self.baraja.repartir(1)[0])
            dealer_puntos = self.dealer.mano_visible.calcular_puntos()
            print(f"Las cartas del dealer son: {self.dealer.mano_visible.cartas} - ({dealer_puntos} puntos)")

        if dealer_puntos > 21:
            print("El dealer se pasó de 21. Ganaste.")
            return 'ganado'
        elif dealer_puntos == puntos:
            print("Es un empate.")
            return 'empate'
        elif dealer_puntos > puntos:
            print("El dealer ganó.")
            return 'perdido'
        else:
            print("Ganaste.")
            return 'ganado'

