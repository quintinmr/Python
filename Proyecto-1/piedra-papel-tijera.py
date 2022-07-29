from tkinter import *
import random 
  
root = Tk() 
  
root.geometry("300x300") 
  
root.title("Rock Paper Scissor Game") 
  
computer_value = { 
    "0":"Piedra", 
    "1":"Papel", 
    "2":"Tijera"
} 
  
def reset_game(): 
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text = "Jugador              ") 
    l3.config(text = "PC") 
    l4.config(text = "") 
  
def button_disable(): 
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"
  
def isrock(): 
    c_v = computer_value[str(random.randint(0,2))] 
    if c_v == "Piedra": 
        match_result = "Empate"
    elif c_v=="Tijeras": 
        match_result = "Gana Jugador"
    else: 
        match_result = "Gana PC"
    l4.config(text = match_result) 
    l1.config(text = "Piedra            ") 
    l3.config(text = c_v) 
    button_disable() 
  
def ispaper(): 
    c_v = computer_value[str(random.randint(0, 2))] 
    if c_v == "Piedra": 
        match_result = "Empate"
    elif c_v=="Tijeras": 
        match_result = "Gana PC"
    else: 
        match_result = "Gana Jugador"
    l4.config(text = match_result) 
    l1.config(text = "Papel           ") 
    l3.config(text = c_v) 
    button_disable() 
  
def isscissor(): 
    c_v = computer_value[str(random.randint(0,2))] 
    if c_v == "Piedra": 
        match_result = "Gana PC"
    elif c_v == "Tijeras": 
        match_result = "Empate"
    else: 
        match_result = "Jugador Gana"
    l4.config(text = match_result) 
    l1.config(text = "Tijeras         ") 
    l3.config(text = c_v) 
    button_disable() 
  
Label(root, 
      text = "Piedra Papel Tijeras", 
      font = "normal 20 bold", 
      fg = "blue").pack(pady = 20) 
  
frame = Frame(root) 
frame.pack() 
  
l1 = Label(frame, 
           text = "Jugador              ", 
           font = 10) 
  
l2 = Label(frame, 
           text = "VS             ", 
           font = "normal 10 bold") 
  
l3 = Label(frame, text = "PC", font = 10) 
  
l1.pack(side = LEFT) 
l2.pack(side = LEFT) 
l3.pack() 
  
l4 = Label(root, 
           text = "", 
           font = "normal 20 bold", 
           bg = "white", 
           width = 15 , 
           borderwidth = 2, 
           relief = "solid") 
l4.pack(pady = 20) 
  
frame1 = Frame(root) 
frame1.pack() 
  
b1 = Button(frame1, text = "Piedra", 
            font = 10, width = 7, 
            command = isrock) 
  
b2 = Button(frame1, text = "Papel ", 
            font = 10, width = 7, 
            command = ispaper) 
  
b3 = Button(frame1, text = "Tijeras", 
            font = 10, width = 7, 
            command = isscissor) 
  
b1.pack(side = LEFT, padx = 10) 
b2.pack(side = LEFT,padx = 10) 
b3.pack(padx = 10) 
  
Button(root, text = "RESET", 
       font = 10, fg = "red", 
       bg = "black", command = reset_game).pack(pady = 20) 
  
root.mainloop()