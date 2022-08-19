import pygame

pygame.init()

# Pantalla de juego
pantalla = pygame.display.set_mode((300,168))
pygame.display.set_caption("Game Ball")

# Creamos la pelota
ball     = pygame.image.load('/home/quintin/Github/Python/Proyecto-1/Ball/ball.png')
ballrect = ball.get_rect()
speed    = [3.5,3.5]
ballrect.move_ip(0,0)

# Creamos la tabla que va a golpear la pelota
bate    = pygame.image.load('/home/quintin/Github/Python/Proyecto-1/Ball/bate.png')
baterect = bate.get_rect()

# Ponemos la tabla en la parte inferior de la pantalla
baterect.move_ip(120,138)

# Bucle principal del juego
jugar = True

while jugar:
    
    # Comprobamos los eventos
    for event in pygame.event.get():

        # Si se ha pulsado el botón de cierre de la ventana
        if event.type == pygame.QUIT:
            jugar = False
        
    # Comprobamos las teclas que se van pulsando
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        baterect = ballrect.move(-3,0)
    
    if keys[pygame.K_RIGHT]:
        baterect = ballrect.move(3,0)
    
    # Si hay colisión
    if baterect.colliderect(ballrect):
        speed[1] = -speed[1]

    ballrect = ballrect.move(speed)

    if ballrect.left < 0 or ballrect.right > pantalla.get_width():
        speed[0] = -speed[0]

    if ballrect.top < 0 or ballrect.bottom > pantalla.get_height():
        speed[1] = -speed[1]

    if ballrect.top < 0: 
        speed[1] = -speed[1]

    # Si la pelota toca el border inferior, has perdido ("Game Over")
    if ballrect.bottom > pantalla.get_height():
        texto = fuente.render("Game Over", True, (125,125,125))
        texto_rect = texto.get_rect()
        texto_x = pantalla.get_width() / 2 - texto_rect.width / 2
        texto_y = pantalla.get_height() / 2 - texto_rect.height / 2
        pantalla.blit(texto, [texto_x, texto_y])
    else:

        # Establecemos el fondo de pantalla
        pantalla.blit(pygame.image.load('/home/quintin/Github/Python/Proyecto-1/Ball/fondo.jpeg'), (0,0))

        # Dibujamos la pelota
        pantalla.blit(ball, ballrect)

        # Dibujo el bate
        pantalla.blit(bate, baterect)

    # Todos los elementos del juego se vuelven a dibujar
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
    

    
