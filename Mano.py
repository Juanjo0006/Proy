# Calcular el valor de una mano


def calcular_puntuacion(mano):
    puntuacion = 0
    ases = 0
    for carta in mano:
        valor = carta[0]
        if valor.isnumeric():
            puntuacion += int(valor)
        elif valor == 'As':
            puntuacion += 11
            ases += 1
        else:
            puntuacion += 10

    # Ajustar el valor de los ases si se pasa de 21
    while puntuacion > 21 and ases > 0:
        puntuacion -= 10
        ases -= 1

    return puntuacion