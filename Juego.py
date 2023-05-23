import Baraja
import Mano

# Jugar al blackjack
def jugar_blackjack():
    baraja_juego = Baraja.crear_baraja()
    mano_jugador = []
    mano_crupier = []

    # Repartir las primeras dos cartas
    Baraja.repartir_carta(baraja_juego, mano_jugador)
    Baraja.repartir_carta(baraja_juego, mano_crupier)
    Baraja.repartir_carta(baraja_juego, mano_jugador)
    Baraja.repartir_carta(baraja_juego, mano_crupier)

    # Mostrar las cartas iniciales
    print('Tu mano:', mano_jugador)
    print('Carta del crupier:', mano_crupier[0])

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

    # Jugar la mano del crupier
    while Mano.calcular_puntuacion(mano_crupier) < 17:
        Baraja.repartir_carta(baraja_juego, mano_crupier)

    # Mostrar las manos finales
    print('Tu mano:', mano_jugador)
    print('Carta del crupier:', mano_crupier)

    # Calcular puntuaciones
    puntuacion_jugador = Mano.calcular_puntuacion(mano_jugador)
    puntuacion_crupier = Mano.calcular_puntuacion(mano_crupier)

    # Determinar el resultado
    if puntuacion_jugador > 21:
        print('Te has pasado de 21. ¡Has perdido!')
    elif puntuacion_crupier > 21:
        print('El crupier se ha pasado de 21. ¡Has ganado!')
    
    elif puntuacion_jugador > puntuacion_crupier:
        print('¡Has ganado!')
    elif puntuacion_crupier > puntuacion_jugador:
        print('Has perdido.')
    else: 
        print('Empate.')

# Iniciar el juego
jugar_blackjack()