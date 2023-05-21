#Maun.py
from Juego import *

def crear_usuario():
    nombre = input("Ingresa tu nombre: ")
    usuario = Usuario(nombre)
    return usuario

def seleccionar_usuario(usuarios):
    print("Selecciona un usuario o crea uno nuevo:\n")
    for i, usuario in enumerate(usuarios):
        print(f"{i + 1}. {usuario.nombre}")
    print(f"{len(usuarios) + 1}. Crear usuario nuevo")
    opcion = input("Elige una opción: ")
    try:
        opcion = int(opcion)
        if opcion > 0 and opcion <= len(usuarios):
            return usuarios[opcion - 1]
        elif opcion == len(usuarios) + 1:
            return crear_usuario()
        else:
            raise ValueError
    except ValueError:
        print("Opción inválida. Intenta de nuevo.")
        return seleccionar_usuario(usuarios)

def mostrar_estadisticas(usuario):
    print(f"Estadísticas de {usuario.nombre}:")
    for i, resultado in enumerate(usuario.resultados[-5:]):
        print(f"Juego {i + 1}: {resultado}")
    input("Presiona Enter para continuar...")

def jugar(usuario):
    juego = Juego(usuario)
    while True:
        limpiar_pantalla()
        print("Bienvenido a Blackjack\n")
        print(f"Jugador: {usuario.nombre}\n")
        print(f"Fichas: {juego.fichas}\n")
        print("1. Nueva partida")
        print("2. Ver estadísticas")
        print("3. Salir\n")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            resultado = juego.jugar()
            if resultado == 'ganaste':
                print("¡Felicidades, ganaste!")
            elif resultado == 'perdiste':
                print("Lo siento, perdiste.")
            elif resultado == 'empate':
                print("Empate.")
            input("Presiona Enter para continuar...")
        elif opcion == '2':
            mostrar_estadisticas(usuario)
        elif opcion == '3':
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
    juego.guardar_resultados()

def main():
    usuarios = Usuario.cargar_usuarios()
    while True:
        limpiar_pantalla()
        print("Bienvenido a Blackjack\n")
        print("1. Seleccionar usuario")
        print("2. Crear usuario nuevo")
        print("3. Salir\n")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            usuario = seleccionar_usuario(usuarios)
            jugar(usuario)
        elif opcion == '2':
            usuario = crear_usuario()
            usuarios.append(usuario)
            jugar(usuario)
        elif opcion == '3':
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
    Usuario.guardar_usuarios(usuarios)

if __name__ == '__main__':
    main()