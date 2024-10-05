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

    fila1 = int(input("Selecciona una fila (0, 1, 2): "))
    columna1 = int(input("Selecciona una columna (0, 1, 2, 3): "))
    
    tablerooculto[fila1][columna1] = tableroreal[fila1][columna1]
    print(f"\nHas seleccionado la carta en la posición ({fila1}, {columna1}): {tableroreal[fila1][columna1]}")
    mostrar_tablero(tablerooculto)
    
    print("\nSelecciona la segunda carta:")
    fila2 = int(input("Fila (0, 1, 2): "))
    columna2 = int(input("Columna (0, 1, 2, 3): "))

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
    seleccionar_carta()

jugarmemorama()
