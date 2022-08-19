import random


# ADIVINA EL NÚMERO VERSIÓN TRIVIAL
x = 0
y = 1000000
a = random.randint(x,y)
b = a + random.randint(x,y)
numero = random.randrange(a,b)

def guess(a):
    
    if a < numero:
        print("Te has quedado por debajo del número")
    elif a > numero:
        print("Te has quedado por encima del número")
    else: print("¡¡¡ENHORABUENA, HAS ACERTADO EL NÚMERO!!!")


def run():

    number = input("INTRODUZCA UN NÚMERO:")
    num    = int(number)

    while True:

        while (num != numero):
            guess(num)
            number = input("INTRODUZCA UN NÚMERO:")
            num    = int(number)
        
        jugar = input("¿Quieres jugar de nuevo(s/n)?: ")
        if jugar.lower() != "s":
            break

if __name__ == '__main__':
    run()



