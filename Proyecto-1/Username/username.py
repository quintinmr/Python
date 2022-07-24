import pygame
import random
import numpy as np
import tkinter as tk
import pyperclip as clipboard
from tkinter import messagebox
from tkinter import ttk, Entry, Button, Text, StringVar, Label, Tk

# Creamos la función que nos va a crear el acrónimo
def username (cadena):
    
    leng = len(cadena)
    username = []
    alfn = cadena.isalnum()

    if alfn == True and leng > 0:
        
        while len(cadena)>0:
            letter = random.choice(cadena)
            num    = random.randrange(0,10000,1)
            username.append(letter)
            username.append(str(num))
            cadena = ''.join((filter(lambda i: i not in username, cadena)))
    
    return username


def run():

    ## CREACIÓN CAJA DE TEXTO ##

    root = Tk()
    root.title("Creación de usuario")
    
    def enviarDatos():
        user = chain.get(1.0, "end-1c")
        usuario = username(user)
        result = ''.join(usuario)
        root.destroy()

        # Caja botón para copiar el username
        v2 = Tk()
        v2.title("Aquí tiene su username")
        botonDeCopiar = Button(v2, text=result, fg="black", font=("Verdana",14), command=clipboard.copy(result))
        botonDeCopiar.grid(row=7,column=0, padx=20, pady=20)
        v2.mainloop()

    chain = Text(root, width=30, height=10)
    chain.grid(row=1,column=0)

    botonDeAceptar = Button(root, text="Aceptar", fg="black", font=("Verdana",14), command=enviarDatos)
    botonDeAceptar.grid(row=7,column=0, padx=20, pady=20)
    root.mainloop()

    

if __name__ == '__main__':
    run()


