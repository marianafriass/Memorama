""" Proyecto: Memorama
Este proyecto consiste en un juego de memoria interactivo llamado "Memorama".
El objetivo es mejorar la memoria y concentración del usuario haciendo coincidir pares de cartas en un tablero.
Dependiendo de la dificultad seleccionada, el tablero contendrá más o menos pares de cartas.
El usuario debe seleccionar cartas, intentar encontrar pares, y el juego termina cuando todos los pares han sido encontrados """


import random

def mostrar_manual():
    """Lee y muestra el contenido del manual del juego."""
    try:
        with open('manual_juego.txt.py', 'r') as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print("El archivo del manual no se encontró.")

def iniciar_tablero(dificultad):
    """Iniciar el tablero de memorama según la dificultad que seleccionó el usuario."""
    if dificultad == 1:
        filas, columnas = 4, 3
        contenido_cartas = ['A', 'B', 'C', 'D', 'E', 'F'] * 2  # 12 cartas (6 pares)
    elif dificultad == 2:
        filas, columnas = 4, 5
        contenido_cartas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] * 2  # 20 cartas (10 pares)
    else:  # Dificultad 3
        filas, columnas = 4, 6
        contenido_cartas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'] * 2  # 24 cartas (12 pares)

    random.shuffle(contenido_cartas)

    # Asegúrate de que el número de cartas es suficiente para llenar el tablero
    cartas = contenido_cartas[:filas * columnas]

    # Poner las cartas en el tablero
    tablero = []
    for i in range(filas):
        tablero.append(cartas[i * columnas:(i + 1) * columnas])

    return tablero

def mostrar_tablero(tablero):
    """Muestra el tablero."""
    for fila in tablero:
        print(" ".join(fila))

def tablerovolteado(tablero_oculto):
    """Muestra el tablero oculto."""
    print("\nTablero boca abajo:")
    mostrar_tablero(tablero_oculto)

def seleccionar_carta(tablero_real, tablero_oculto, cartas_seleccionadas):
    """El jugador puede comenzar a seleccionar dos cartas del tablero."""
    primera_carta = None

    for i in range(2):
        while True:
            try:
                fila = int(input(f"\nSelecciona una fila del 0 al {len(tablero_real) - 1}: "))
                columna = int(input(f"Selecciona una columna del 0 al {len(tablero_real[0]) - 1}: "))
                if (0 <= fila < len(tablero_real)) and (0 <= columna < len(tablero_real[0])):
                    if (fila, columna) in cartas_seleccionadas:
                        print("Ya has seleccionado esa carta, intenta de nuevo.")
                    else:
                        break
                else:
                    print("Posición inválida, intenta de nuevo.")
            except ValueError:
                print("Entrada inválida, intenta de nuevo.")

        # Revelar la carta seleccionada
        tablero_oculto[fila][columna] = tablero_real[fila][columna]
        print(f"Haz seleccionado la carta en la posición ({fila}, {columna}): "
              f"{tablero_real[fila][columna]}\n")
        mostrar_tablero(tablero_oculto)

        if i == 0:
            primera_carta = (fila, columna)

    fila1, columna1 = primera_carta
    fila2, columna2 = (fila, columna)

    # Comprobar si las cartas seleccionadas son iguales
    if tablero_real[fila1][columna1] == tablero_real[fila2][columna2]:
        print("Correcto!\n")
        cartas_seleccionadas.add(primera_carta)
        cartas_seleccionadas.add((fila2, columna2))
        return True
    else:
        print("No son par, intenta de nuevo\n")
        # Volver a ocultar las cartas seleccionadas
        tablero_oculto[fila1][columna1] = 'X'
        tablero_oculto[fila2][columna2] = 'X'
        return False

def jugar_memorama():
    """Inicia el juego de memorama."""
    print("Bienvenido al memorama\n")
    mostrar_manual()  # Muestra el manual al inicio del juego

    while True:
        try:
            dificultad = int(input("\nSelecciona la dificultad: \n 1. Fácil\n 2. Medio\n 3. Difícil\n\n"))
            if dificultad in [1, 2, 3]:
                break
            else:
                print("Dificultad inválida, intenta de nuevo.")
        except ValueError:
            print("Entrada inválida, intenta de nuevo.")

    tablero_real = iniciar_tablero(dificultad)
    tablero_oculto = [['X'] * len(tablero_real[0]) for _ in range(len(tablero_real))]
    cartas_seleccionadas = set()
    intentos = 0

    tablerovolteado(tablero_oculto)

    total_pares = (len(tablero_real) * len(tablero_real[0])) // 2  # Total de pares a encontrar

    while len(cartas_seleccionadas) < total_pares * 2:  # Se multiplica por 2 porque se cuenta cada carta
        acierto = seleccionar_carta(tablero_real, tablero_oculto, cartas_seleccionadas)
        intentos += 1

    print(f"¡Felicidades! Has encontrado todos los pares en {intentos} intentos.")

def pruebas():
    """Función para realizar pruebas sobre las funcionalidades del juego."""
    # Test para iniciar_tablero
    tablero = iniciar_tablero(1)
    assert len(tablero) == 4  # Verifica que el tablero tenga 4 filas para dificultad 1
    assert len(tablero[0]) == 3  # Verifica que cada fila tenga 3 cartas

    tablero = iniciar_tablero(2)
    assert len(tablero) == 4  # Verifica que el tablero tenga 4 filas para dificultad 2
    assert len(tablero[0]) == 5  # Verifica que cada fila tenga 5 cartas

    tablero = iniciar_tablero(3)
    assert len(tablero) == 4  # Verifica que el tablero tenga 4 filas para dificultad 3
    assert len(tablero[0]) == 6  # Verifica que cada fila tenga 6 cartas

    # Test para seleccionar_carta
    tablero_real = [['A', 'B', 'C', 'D', 'E', 'F'], 
                    ['G', 'H', 'I', 'J', 'K', 'L'], 
                    ['A', 'B', 'C', 'D', 'E', 'F'], 
                    ['G', 'H', 'I', 'J', 'K', 'L']]
    tablero_oculto = [['X'] * 6 for _ in range(4)]
    cartas_seleccionadas = set()

    # Llamada a la función
    acierto = seleccionar_carta(tablero_real, tablero_oculto, cartas_seleccionadas)
    assert acierto in [True, False]  # La función debe devolver True o False

# Ejecutar las pruebas al inicio
pruebas()  
# Iniciar el juego después de las pruebas
jugar_memorama()

