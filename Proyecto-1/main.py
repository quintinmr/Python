from tkinter import *
from tkinter import ttk
import pygame


# Ventana del menú desplegable
ventana = Tk()
ventana.title("MULTIJUEGO")
ventana.geometry('700x700')

# Lista desplegable
lista = ttk.Combobox(ventana, width=20)
lista.place(x=175, y=330)

# Función que ejecuta el juego seleccionado
def jugar():

    if lista.current() == 0:
        exec(open("/home/quintin/Github/Python/Proyecto-1/Adivina/adivina.py").read())
    elif lista.current() == 1:
        exec(open("/home/quintin/Github/Python/Proyecto-1/Ball/ball.py").read())
    elif lista.current() == 2:
        exec(open("/home/quintin/Github/Python/Proyecto-1/JuegoDeLaVida/juegoVida.py").read())
    elif lista.current() == 3:
        exec(open("/home/quintin/Github/Python/Proyecto-1/Snake/snake.py").read())
    elif lista.current() == 4:
        exec(open("/home/quintin/Github/Python/Proyecto-1/Username/username.py").read())

# Lista de opciones
options = ["Adivina", "Ball", "Juego de la Vida", "Snake", "Username"]

# Insertar valores 
lista['values'] = options

# Botón de jugar
Button(ventana, text="JUGAR", bg='blue', command=jugar).place(x=533,y=326)
# Botón de salir
Button(ventana, text="EXIT", bg='gray', command=ventana.quit()).place(x=200,y=450)

ventana.mainloop()
