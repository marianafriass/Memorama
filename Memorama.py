tableroreal = [
    ['A', 'B', 'C', 'D'],
    ['A', 'B', 'C', 'D'],
    ['E', 'F', 'G', 'H']
]

tablerooculto = [
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X']
]

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))

def tablerovolteado():
    print("Tablero boca abajo:")
    mostrar_tablero(tablerooculto)

def seleccionar_carta():
    while True:
        try:
            fila1 = int(input("Selecciona una fila (0, 1, 2): "))
            columna1 = int(input("Selecciona una columna (0, 1, 2, 3): "))
            if 0 <= fila1 <= 2 and 0 <= columna1 <= 3:
                break
            else:
                print("Posición inválida, intenta de nuevo.")
        except ValueError:
            print("Entrada inválida, intenta de nuevo.")

    tablerooculto[fila1][columna1] = tableroreal[fila1][columna1]
    print(f"\nHas seleccionado la carta en la posición ({fila1}, {columna1}): {tableroreal[fila1][columna1]}")
    mostrar_tablero(tablerooculto)

    while True:
        try:
            fila2 = int(input("Selecciona una segunda fila (0, 1, 2): "))
            columna2 = int(input("Selecciona una segunda columna (0, 1, 2, 3): "))
            if 0 <= fila2 <= 2 and 0 <= columna2 <= 3:
                break
            else:
                print("Posición inválida, intenta de nuevo.")
        except ValueError:
            print("Entrada inválida, intenta de nuevo.")

    tablerooculto[fila2][columna2] = tableroreal[fila2][columna2]
    print(f"\nSegunda carta seleccionada en la posición ({fila2}, {columna2}): {tableroreal[fila2][columna2]}")
    mostrar_tablero(tablerooculto)

    if tableroreal[fila1][columna1] == tableroreal[fila2][columna2]:
        print("¡Correcto!")
    else:
        print("No es un par, intenta de nuevo.")
        tablerooculto[fila1][columna1] = 'X'
        tablerooculto[fila2][columna2] = 'X'

    mostrar_tablero(tablerooculto)

def jugarmemorama():
    print("Bienvenido al memorama")
    tablerovolteado()
    while True:
        seleccionar_carta()
        salir = input("¿Quieres seguir jugando? (s/n): ").lower()
        if salir == 'n':
            print("Gracias por jugar.")
            break

jugarmemorama()

