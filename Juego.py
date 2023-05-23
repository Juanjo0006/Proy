import Baraja
import Mano

# Jugar al blackjack
def jugar_blackjack(nombre_usuario=None):
    baraja_juego = Baraja.crear_baraja()
    mano_jugador = []
    mano_dealer = []

    # Repartir las primeras dos cartas
    Baraja.repartir_carta(baraja_juego, mano_jugador)
    Baraja.repartir_carta(baraja_juego, mano_dealer)
    Baraja.repartir_carta(baraja_juego, mano_jugador)
    Baraja.repartir_carta(baraja_juego, mano_dealer)

    # Mostrar las cartas iniciales
    print('Tu mano:', mano_jugador)
    print('Carta del dealermano_dealer:', mano_dealer[0])

    # Jugar la mano del jugador
    while True:
        opcion = input('¿Quieres pedir otra carta? (s/n): ')
        if opcion.lower() == 's':
            Baraja.repartir_carta(baraja_juego, mano_jugador)
            print('Tu mano:', mano_jugador)
            if Mano.calcular_puntuacion(mano_jugador) > 21:
                print('Te has pasado de 21. ¡Has perdido!')
                return
        else:
            break

    # Jugar la mano del dealermano_dealer
    while Mano.calcular_puntuacion(mano_dealer) < 17:
        Baraja.repartir_carta(baraja_juego, mano_dealer)

    # Mostrar las manos finales
    print('Tu mano:', mano_jugador)
    print('Carta del dealermano_dealer:', mano_dealer)

    # Calcular puntuaciones
    puntuacion_jugador = Mano.calcular_puntuacion(mano_jugador)
    puntuacion_dealermano_dealer = Mano.calcular_puntuacion(mano_dealer)

    # Determinar el resultado
    if puntuacion_jugador > 21:
        print('Te has pasado de 21. ¡Has perdido!')
    elif puntuacion_dealermano_dealer > 21:
        print('El dealermano_dealer se ha pasado de 21. ¡Has ganado!')
    
    elif puntuacion_jugador > puntuacion_dealermano_dealer:
        print('¡Has ganado!')
    elif puntuacion_dealermano_dealer > puntuacion_jugador:
        print('Has perdido.')
    else: 
        print('Empate.')

# Iniciar el juego
jugar_blackjack()
