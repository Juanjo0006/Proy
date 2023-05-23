import Baraja
import Mano

def mostrar_menu():
    print("Bienvenido al Blackjack")
    print("1. Jugar")
    print("2. Estadísticas de puntos")
    print("3. Salir")

def obtener_nombre_usuario():
    nombre = input("Ingrese su nombre de usuario: ")
    archivo = open("usuarios.txt", "w")
    archivo.write(nombre)
    archivo.close()

def obtener_nombre_guardado():
    try:
        archivo = open("usuarios.txt", "r")
        nombre = archivo.read()
        archivo.close()
        return nombre
    except FileNotFoundError:
        return None

def registrar_puntos(nombre, puntos):
    archivo = open("estadisticas.txt", "a")
    archivo.write(nombre + "," + str(puntos) + "\n")
    archivo.close()

def mostrar_estadisticas():
    try:
        archivo = open("estadisticas.txt", "r")
        print("Estadísticas de puntos:")
        for linea in archivo:
            nombre, puntos = linea.strip().split(",")
            print(nombre + ": " + puntos)
        archivo.close()
    except FileNotFoundError:
        print("No hay estadísticas de puntos disponibles.")

def jugar():
    nombre_usuario = obtener_nombre_guardado()
    if nombre_usuario is None:
        obtener_nombre_usuario()
        nombre_usuario = obtener_nombre_guardado()

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
    print('Carta del dealer:', mano_dealer[0])

    # Jugar la mano del jugador
    while True:
        opcion = input('¿Quieres pedir otra carta? (s/n): ')
        if opcion.lower() == 's':
            Baraja.repartir_carta(baraja_juego, mano_jugador)
            print('Tu mano:', mano_jugador)
            if Mano.calcular_puntuacion(mano_jugador) > 21:
                print('Te has pasado de 21. ¡Has perdido!')
                registrar_puntos(nombre_usuario, 0)
                return
        else:
            break

    # Jugar la mano del dealer
    while Mano.calcular_puntuacion(mano_dealer) < 17:
        Baraja.repartir_carta(baraja_juego, mano_dealer)

    # Mostrar las manos finales
    print('Tu mano:', mano_jugador)
    print('Carta del dealer:', mano_dealer)

    # Calcular puntuaciones
    puntuacion_jugador = Mano.calcular_puntuacion(mano_jugador)
    puntuacion_dealer = Mano.calcular_puntuacion(mano_dealer)

    # Determinar el resultado
    if puntuacion_jugador > 21:
        print('Te has pasado de 21. ¡Has perdido!')
        registrar_puntos(nombre_usuario, 0)
    elif puntuacion_dealer > 21:
        print('El dealer se ha pasado de 21. ¡Has ganado!')
    
    elif puntuacion_jugador > puntuacion_dealer:
        print('¡Has ganado!')
    elif puntuacion_dealer > puntuacion_jugador:
        print('Has perdido.')
    else: 
        print('Empate.')

# Iniciar el juego
pass


def main():
    nombre_usuario = obtener_nombre_guardado()

    if nombre_usuario is None:
        obtener_nombre_usuario()
        nombre_usuario = obtener_nombre_guardado()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            jugar()
        elif opcion == "2":
            mostrar_estadisticas()
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()