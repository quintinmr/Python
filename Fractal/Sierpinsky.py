# Este programa está destinado al cálculo y representación del
# triángulo de Sierpinsky

# La idea es la siguiente:
    # 1. Partimos de un triángulo cualquiera
    # 2. Escogemos un punto dentro del triángulo, aleatorio
    # 3. Escogemos al azar uno de los tres vértices del triángulo inicial
    # 4. Calculamos el punto medio del segmento que los une
    # 5. Elegimos otro vértice al azar y calculamos el punto medio
    #    del segmento que une el vértice 
    # 6. Hacemos lo mismo iteradamente

import tkinter as tk
from tkinter import *
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random as rng
import pyperclip as clipboard

# Modelamos el objeto de la clase punto
class Punto(object):

    def __init__(self, x, y):

        self.x = x
        self.y = y

class Programa(object):

    def __init__(self):

        ## CREACIÓN CAJA DE TEXTO ##
        self.root = Tk()
        self.root.title("Triángulo de Sierpinsky")
        
        self.it_label = tk.Label(self.root, text = 'Iteraciones', font = ('calibre',10,'bold'))
        self.it_label.grid(row=1,column=0)

        self.iteraciones_var = tk.StringVar()

        self.it_entry = tk.Entry(self.root, textvariable = self.iteraciones_var, font = ('calibre',10,'normal'))
        self.it_entry.grid(row=1,column=1)

        self.botonDeAceptar = Button(self.root, text="Ejecutar Programa", fg="black", font=("Verdana",14), command=self.run)
        self.botonDeAceptar.grid(row=7,column=0, padx=20, pady=20)
        self.root.mainloop()

    def getIteraciones(self):

        iteraciones = self.iteraciones_var.get()
        return iteraciones

    def run(self):

        iteraciones = int((self.getIteraciones()).strip(''))
        print(iteraciones)

        # Arrays donde vamos a ir guardado las coordenadas x e y de los puntos
            # medios que vayamos obteniendo
        arrayX = []
        arrayY = []

        # Coordenadas del triángulo inicial (invención del autor)

        T1 = Punto(0,0)
        T2 = Punto(1,0)
        T3 = Punto(0.5,np.sqrt(3)/2)

        # Punto al azar dentro del triángulo
        p = Punto(0.5, 0.65)

        # Guardamos las coordenadas del punto
        arrayX.append(p.x)
        arrayY.append(p.y)
        
        # Array de números aleatorios de valores entre 0 y 1 para elegir
        # aleatoriamente los vértices en cada iteración
        vertices = []
        vertices = rng(iteraciones)

        m = Punto(0,0)
        # Bucle principal donde se calcularán los puntos medios
        
        if iteraciones is not None:
            for i in range(iteraciones):

                if vertices[i] < 1/3:
                    verticex = T1.x
                    verticey = T1.y
                elif 1/3 < vertices[i] < 2/3:
                    verticex = T2.x
                    verticey = T2.y
                else:
                    verticex = T3.x
                    verticey = T3.y
                
                if i == 0:
                    m.x = (verticex + p.x)/2
                    m.y = (verticey + p.y)/2

                else:
                    m.x = (verticex + m.x)/2
                    m.y = (verticey + m.y)/2
                
                # Guardamos los puntos en los arrays de puntos medios
                arrayX.append(m.x)
                arrayY.append(m.y)

        self.root.destroy()

        # Dibujamos
        plt.plot(arrayX, arrayY, 'g ,')
        plt.show()


programa1 = Programa()
programa1.run()
