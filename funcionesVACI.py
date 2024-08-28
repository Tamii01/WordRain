from juegoprincipal import *
from configuracion import *
from funcionesSeparador import *

import random
import math
import pygame

def lectura(archivo, lista):
    f = archivo.readlines()
    for linea in f:
        lista.append(linea[:-1])
    return linea

def actualizar(silabasEnPantalla,posiciones,listaDeSilabas):
    silaba= nuevaSilaba(listaDeSilabas)
    silabasEnPantalla.append(silaba)
    x= random.randrange(3, ANCHO-85)
    y= 0
    pos=[x, y]
    posiciones.append(pos)
    i=0
    while(i<len(posiciones)):
        if posiciones[i][1]>=ALTO-130:
            silabasEnPantalla.pop(i)
            posiciones.pop(i)
        else:
            posiciones[i][1]+=10
        i+=1

def nuevaSilaba(silabas):
    n = random.randrange(len(silabas))
    pal = silabas[n]
    return pal.lower()

def quitar(candidata, silabasEnPantalla, posiciones):
    silabas = dameSilabas(candidata)
    for elem in silabas:
        i=0
        while (i<len(silabasEnPantalla)):
            if elem==silabasEnPantalla[i]:
                silabasEnPantalla.pop(i)
                posiciones.pop(i)
            i+=1

def dameSilabas(candidata):
    silabas=separador(candidata)
    lista=silabas.split("-")
    return lista

def esValida(candidata, silabasEnPantalla, lemario):
    silabaCand=dameSilabas(candidata)
    for i in silabaCand:
        if i not in silabasEnPantalla:
            return False
        if candidata not in lemario:
            return False
        return True

def Puntos(candidata):
    puntos=0
    for i in range(len(candidata)):
        if candidata[i]=="a" or candidata[i]=="e" or candidata[i]=="i" or candidata[i]=="o" or candidata[i]=="u":
            puntos=puntos+1
        else:
                if candidata[i]=="j" or candidata[i]=="k" or candidata[i]=="q" or candidata[i]=="w" or candidata[i]=="x" or candidata[i]=="y" or candidata[i]=="z":
                    puntos=puntos+5
                else:
                    if candidata[i]!="j" or candidata[i]!="k" or candidata[i]!="q" or candidata[i]!="w" or candidata[i]!="x" or candidata[i]!="y" or candidata[i]!="z":
                        puntos=puntos+2
        return puntos


def procesar(candidata, silabasEnPantalla, posiciones, lemario):
    valida = esValida(candidata, silabasEnPantalla, lemario)
    pygame.mixer.init()
    if valida == True:
        correcto = pygame.mixer.Sound ('correcto.wav') # Sonido de palabra correcta
        correcto.play()
        quitar(candidata, silabasEnPantalla, posiciones)
        return Puntos(candidata)
    else:
        correcto = pygame.mixer.Sound ('incorrecto.wav') # Sonido de palabra incorrecta
        correcto.play()
        quitar(candidata, silabasEnPantalla, posiciones)
        return Puntos(candidata)-5