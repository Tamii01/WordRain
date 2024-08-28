#! /usr/bin/env python
import os, random, sys, math

import pygame

from pygame.locals import *

from configuracion import *
from extras import *
from funcionesSeparador import *
from funcionesVACI import *
from menufinal import Menu


#Funcion principal
def main():
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load('musicajuego.mp3') #Iniciador de música
        pygame.mixer.music.play (-1)

        #Preparar la ventana
        pygame.display.set_caption("Rapido...")
        screen = pygame.display.set_mode((ANCHO, ALTO))
        background = pygame.image.load("background4.jpg").convert()


        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial

        puntos = 0
        candidata = ""
        silabasEnPantalla = []
        posiciones = []
        listaDeSilabas=[]
        lemario=[]

        archivo= open("silabas.txt","r")
        lectura(archivo, listaDeSilabas)

        archivo2= open("lemario.txt","r")
        lectura(archivo2, lemario)

        dibujar(screen, candidata, silabasEnPantalla, posiciones, puntos,segundos)

        while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()


            if True:
            	fps = 2

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    candidata += letra
                    if e.key == K_BACKSPACE:
                        candidata = candidata[0:len(candidata)-1]
                    if e.key == K_RETURN:
                        puntos += procesar(candidata, silabasEnPantalla, posiciones, lemario)
                        candidata = ""


            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000

            #Limpiar pantalla anterior

            screen.blit(background, [0, 0])

            #Dibujar de nuevo todo
            dibujar(screen, candidata, silabasEnPantalla, posiciones, puntos, segundos)

            pygame.display.flip()

            actualizar(silabasEnPantalla, posiciones, listaDeSilabas)



        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return

#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()


