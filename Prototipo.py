# import random


# #Cartas
# # Crear una baraja de cartas
# def crear_baraja():
#     baraja = []
#     palos = ['Corazones', 'Diamantes', 'Picas', 'Tréboles']
#     valores = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
#     for palo in palos:
#         for valor in valores:
#             baraja.append((valor, palo))
#     return baraja

# # Calcular el valor de una mano
# def calcular_puntuacion(mano):
#     puntuacion = 0
#     ases = 0
#     for carta in mano:
#         valor = carta[0]
#         if valor.isnumeric():
#             puntuacion += int(valor)
#         elif valor == 'As':
#             puntuacion += 11
#             ases += 1
#         else:
#             puntuacion += 10

#     # Ajustar el valor de los ases si se pasa de 21
#     while puntuacion > 21 and ases > 0:
#         puntuacion -= 10
#         ases -= 1

#     return puntuacion

# # Repartir una carta de la baraja a una mano
# def repartir_carta(baraja, mano):
#     carta = random.choice(baraja)
#     baraja.remove(carta)
#     mano.append(carta)

# # Jugar al blackjack
# def jugar_blackjack():
#     baraja = crear_baraja()
#     mano_jugador = []
#     mano_crupier = []

#     # Repartir las primeras dos cartas
#     repartir_carta(baraja, mano_jugador)
#     repartir_carta(baraja, mano_crupier)
#     repartir_carta(baraja, mano_jugador)
#     repartir_carta(baraja, mano_crupier)

#     # Mostrar las cartas iniciales
#     print('Tu mano:', mano_jugador)
#     print('Carta del crupier:', mano_crupier[0])

#     # Jugar la mano del jugador
#     while True:
#         opcion = input('¿Quieres pedir otra carta? (s/n): ')
#         if opcion.lower() == 's':
#             repartir_carta(baraja, mano_jugador)
#             print('Tu mano:', mano_jugador)
#             if calcular_puntuacion(mano_jugador) > 21:
#                 print('Te has pasado de 21. ¡Has perdido!')
#                 return
#         else:
#             break

#     # Jugar la mano del crupier
#     while calcular_puntuacion(mano_crupier) < 17:
#         repartir_carta(baraja, mano_crupier)

#     # Mostrar las manos finales
#     print('Tu mano:', mano_jugador)
#     print('Carta del crupier:', mano_crupier)

#     # Calcular puntuaciones
#     puntuacion_jugador = calcular_puntuacion(mano_jugador)
#     puntuacion_crupier = calcular_puntuacion(mano_crupier)

#     # Determinar el resultado
#     if puntuacion_jugador > 21:
#         print('Te has pasado de 21. ¡Has perdido!')
#     elif puntuacion_crupier > 21:
#         print('El crupier se ha pasado de 21. ¡Has ganado!')
    
#     elif puntuacion_jugador > puntuacion_crupier:
#         print('¡Has ganado!')
#     elif puntuacion_crupier > puntuacion_jugador:
#         print('Has perdido.')
#     else: 
#         print('Empate.')

# # Iniciar el juego
# jugar_blackjack()

from Baraja import baraja
from Mano import mano
from Juego import juego

