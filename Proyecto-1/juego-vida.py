import pygame
import numpy as np
import time

pygame.init()

# Ancho y alto de la pantalla
width, height = 1000, 1000

# Creación de la pantalla
screen = pygame.display.set_mode((height,width))

#Color del fondo
bg = 25,25,25  
# Pintar fondo 
screen.fill(bg)

# Número de celdas
ncx, ncy = 50, 50

# Dimensiones de la celda
dimCW = width/ncx
dimCH = height/ncy

# Estado de las celdas. Vivas = 1; Muertas = 0
gameState = np.zeros((ncx, ncy))

# Autómata móvil
gameState[21,21] = 1
gameState[22,22] = 1
gameState[22,23] = 1
gameState[21,23] = 1
gameState[20,23] = 1

# Control de la ejecución del juego
pauseExect = False

# Para campo infinito
while True:

    # En cada iteración hacemos una copia del estado
    newGameState = np.copy(gameState)

    screen.fill((bg))

    # Para que el sistema se tome un pequeño respiro entre display y display
    time.sleep(0.1)

    # Registramos eventos de teclado y ratón
    ev = pygame.event.get()

    for event in ev:

        # Detectamos si se presiona una tecla
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect
        
        # Detectamos si se presiona el ratón
        mouseClick = pygame.mouse.get_pressed()

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX/dimCW)), int(np.floor(posY/dimCH))
            newGameState[celX, celY] = 1

    for y in range(0,ncx):
        for x in range(0,ncy):

            # Calculamos el número de vecinos cercanos
            # Aplicamos estrategia toroidal

            if not pauseExect:
                n_neigh = gameState[(x-1)%ncx, (y-1)%ncy] + \
                        gameState[(x)%ncx  , (y-1)%ncy] + \
                        gameState[(x+1)%ncx, (y-1)%ncy] + \
                        gameState[(x-1)%ncx  , (y)%ncy] + \
                        gameState[(x+1)%ncx  , (y)%ncy] + \
                        gameState[(x-1)%ncx, (y+1)%ncy] + \
                        gameState[(x)%ncx  , (y+1)%ncy] + \
                        gameState[(x+1)%ncx, (y+1)%ncy]

            # Rule 1: Una célula muerta con exáctamente 3 vecinas vivas, "revive"
            if gameState[x,y] == 0 and n_neigh == 3:
                newGameState[x,y] = 1
            # Rule 2: Una célula viva con menos de 2 o más de 3 vecinas vivas, "muere"
            elif gameState[x,y] == 1 and  (n_neigh < 2 or n_neigh > 3):
                newGameState[x,y] = 0

            poly = [((x)   * dimCW, y     * dimCH),
                    ((x+1) * dimCW, y     * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x)   * dimCW, (y+1) * dimCH)]

            # Dibujamos la celda para cada par de x e y
            if newGameState[x,y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 255)

    # Actualizamos el estado del juego
    gameState = np.copy(newGameState)

    # Actualizamos pantalla 
    pygame.display.flip()