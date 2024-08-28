import pygame
from pygame.locals import *
from juegoprincipal import *



class Menu:
##    Representa un menú con opciones para un juego

    def __init__(self, opciones):
        self.opciones = opciones
        self.font = pygame.font.Font('8-BIT WONDER.ttf', 40)
        self.seleccionado = 0 #comienzo de opcion seleccionada
        self.total = len(self.opciones)
        self.mantiene_pulsado = False
        pygame.mixer.init()
        pygame.mixer.music.load('musicafinal.mp3') #Iniciador de música
        pygame.mixer.music.play (-1)



    def actualizar(self):
##        Altera el valor de 'self.seleccionado' con los direccionales

        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:

                # Invoca a la función asociada a la opción.
                titulo, funcion = self.opciones[self.seleccionado]
                print ("Selecciona la opción: "), titulo
                funcion()

        # procura que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]


    def imprimir(self, screen):
##        Imprime sobre 'screen' el texto de cada opción del menú.

        total = self.total
        indice = 0
        altura_de_opcion = 50
        # Posicion de las opciones
        x = 214
        y = 370

        for (titulo, funcion) in self.opciones:
            if indice == self.seleccionado:
                color = (97, 106, 107 )
            else:
                color = (255, 255, 255)

            imagen = self.font.render(titulo, -2, color)
            posicion = (x, y + altura_de_opcion * indice)
            indice += 1
            screen.blit(imagen, posicion)


def jugar_de_nuevo():
    main ()
    return


def salir_del_programa():
    pygame.quit()



if __name__ == '__main__':

    salir = False
    opciones = [
        ("Jugar de nuevo", jugar_de_nuevo),
        ("        Salir", salir_del_programa)
        ]

    pygame.font.init()
    screen = pygame.display.set_mode((945, 675)) # Medida de la pantalla

    fondo = pygame.image.load("background5.jpg").convert() # Imagen de fondo
    width = 945
    x = 0

    fuentetitulomenu = pygame.font.Font('8-BIT WONDER.ttf', 90) #Tamano del titulo principal
    titulomenu = fuentetitulomenu.render ('Game Over',0,(255,255,255)) # Color de letras del titulo principal
    fuentepuntosfinal = pygame.font.Font ("Eight-Bit Madness.ttf", 70)
    puntosfinal = fuentepuntosfinal.render('PUNTAJE: '+ str(puntos),0,(242, 44, 44))
    menu = Menu(opciones)


    while not salir:

        for e in pygame.event.get():
            if e.type == QUIT:
                salir = True
                pygame.quit()

        x_relativa = x % fondo.get_rect().width
        screen.blit(fondo, (x_relativa - fondo.get_rect().width , 0))
        if (x_relativa < width):
            screen.blit(fondo, (x_relativa, 0))
        x -=1

        screen.blit (titulomenu, (82,130)) # Posicion del titulo principal
        screen.blit (puntosfinal, (100, 290))# Posicion de PUNTOS
        menu.actualizar()
        menu.imprimir(screen)

        pygame.display.flip()
        pygame.time.delay(10)

