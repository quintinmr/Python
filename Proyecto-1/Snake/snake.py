import pygame       # importamos la biblioteca pygame. Ideal para crear juegos en python
import numpy as np  # importamos la biblioteca numpy, a la que podremos referirnos con np. Para cálculos matemáticos, nº aleatorios...
import sys
import time
from pygame.locals import *


pygame.init()

## Creamos la clase Juego

class Juego(object):

    # Inicio del juego
    def __init__(self, ancho, alto):
        pygame.display.set_caption("Snake")
        self.ancho = ancho
        self.alto  = alto
        self.display_juego = pygame.display.set_mode((ancho, alto+100))
        self.bg = pygame.image.load('img/fondo.jpg')
        self.colision = False
        self.score = 0
        self.font = pygame.font.SysFont('Ubuntu', 20)
    
    def display_ui (self, record):
        self.display_juego.fill((255,255,255))
        score_text = self.font.render('RESULTADO:', True, (0,0,0))
        score_num  = self.font.render(str(self.score), True, (0,0,0))
        record_text= self.font.render('MEJOR:', True, (0,0,0))
        record_num = self.font.render(str(record), True, (0,0,0))

        pygame.draw.rect(self.display_juego, (200,200,200), (0,self.alto, self.ancho, 0))

        # Para colocar los elementos hacemos uso de la función blit
        self.display_juego.blit(score_text, (45,480))
        self.display_juego.blit(score_num,  (45,480))
        self.display_juego.blit(record_text, (45,480))
        self.display_juego.blit(record_num, (45,480))
        self.display_juego.blit(self.bg, (0,0))

    def obtener_record(self, score, record):
        return score if score >= record else record
    
class Jugador(object):

    def __init__(self):
        self.x = 100
        self.y = 100
        self.posicion = []
        self.posicion.append([self.x, self.y])
        self.manzanas = 1
        self.comida   = False
        self.imagen   = pygame.image.load('img/cuerpo_serpiente.png')
        self.cambio_x = 20
        self.cambio_y = 0
        self.direccion= [1,0]
    
    def refrescar_pos(self, x, y):

        if self.posicion[-1][0] != x or self.posicion[-1][0] != y:
            if self.manzanas > 1:
                for i in range(self.manzanas -1):
                    self.posicion[i][0], self.posicion[i][1] = self.posicion[i+1]
            
            self.posicion[-1][0] = x
            self.posicion[-1][1] = y

    def hacer_movimientos(self, x, y, juego, comida):

        array = [self.cambio_x, self.cambio_y]

        if self.comida:
            self.posicion.append([self.x, self.y])
            self.comida = False
            self.manzanas += 1

        for e in pygame.event.get():

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT and self.direccion != [1,0]:
                    array = [-20,0]
                    self.direccion = [-1,0]
                elif e.key == pygame.K_RIGHT and self.direccion != [-1,0]:
                    array = [20,0]
                    self.direccion = [1,0]
                elif e.key == pygame.K_UP and self.direccion != [0,-1]:
                    array = [0,-20]
                    self.direccion = [0,1]
                elif e.key == pygame.K_DOWN and self.direccion != [0,1]:
                    array = [0,20]
                    self.direccion = [0,-1]


        self.cambio_x, self.cambio_y = array
        self.x = x + self.cambio_x
        self.y = y + self.cambio_y

        if self.x < 0 or self.x > juego.ancho-20 \
            or self.y < 0 or self.y > juego.alto-20 \
            or [self.x, self.y] in self.posicion:
            juego.colision = True
        
        comida.comer(self, juego)
        self.refrescar_pos(self.x, self.y)
    
    def display_jugador(self, x, y, juego):
        self.posicion[-1][0] = x
        self.posicion[-1][1] = y

        if juego.colision == False:
            for i in range(self.manzanas):
                x_temp, y_temp = self.posicion[len(self.posicion) -1 -i]
                juego.display_juego.blit(self.imagen, (x_temp, y_temp))
        
class Food(object):

    def __init__(self):
        self.x_food = 200
        self.y_food = 200
        self.imagen = pygame.image.load('img/comida.png')

    def comida_coor(self, juego, jugador):

        x_rand = np.random.choice(list(range(0,juego.ancho, 20)))
        self.x_food = x_rand
        y_rand = np.random.choice(list(range(0,juego.alto, 20)))
        self.y_food = y_rand
    
    def display_comida(self, x, y, juego):
        juego.display_juego.blit(self.imagen, (x,y))
    
    def comer (self, jugador, juego):
        if jugador.x == self.x_food and jugador.y == self.y_food:
            self.comida_coor(juego, jugador)
            jugador.comida = True
            juego.score += 1

def run():
    pygame.init()
    record = 0
    clock  = pygame.time.Clock()
    while True:
        juego = Juego(1000,1000)
        jugador = Jugador()
        comida = Food()

        juego.display_ui(record)
        jugador.display_jugador(jugador.x, jugador.y, juego)
        comida.display_comida(comida.x_food, comida.y_food, juego)
        pygame.display.update()

        while not juego.colision:
            jugador.hacer_movimientos(jugador.x, jugador.y, juego, comida)
            record = juego.obtener_record(juego.score, record)
            juego.display_ui(record)
            jugador.display_jugador(jugador.x, jugador.y, juego)
            comida.display_comida(comida.x_food, comida.y_food, juego)
            pygame.display.update()
            clock.tick(10)

if __name__ == '__main__':
    run()
