import pygame
from game import *

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 50, 50) #Medidas del cursor
        self.offset = - 150 #Movimiento del cursor; para la derecha reducir el numero, para la izquierda aumentar el numero



    def draw_cursor(self):
        self.game.draw_text('*', 35, self.cursor_rect.x, self.cursor_rect.y) #Gráfico del cursor

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h +  30 #Cambiar posicion de los palabras del menu principal (más arriba o más abajo)
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 80
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 130
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
        pygame.mixer.music.load('musicainicio.mp3') #Iniciador de música
        pygame.mixer.music.play (-1) #El numero indica la repeticion de la musica #(-1) = loop



    def display_menu(self):
        self.run_display = True
        width = 945
        x = 0
        while self.run_display:
            self.game.check_events()
            self.check_input()

            #Imagen de fondo del menu principal
            background = pygame.image.load("background2.jpg").convert()
            self.game.display.fill(self.game.BLACK)
            self.game.display.blit(background,(x,0))
            x_relativa = x % background.get_rect().width
            self.game.display.blit(background, (x_relativa - background.get_rect().width, 0))
            if (x_relativa < width):
                self.game.display.blit(background, (x_relativa, 0))
            x -= 5

            self.game.draw_text('UNIBLES', 115, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 100) #TAMAÑO DE LETRAS
            self.game.draw_text("Jugar", 40, self.startx, self.starty) #Tamaño de la opcion JUGAR
            self.game.draw_text("Opciones", 40, self.optionsx, self.optionsy) #Tamaño de la opcion OPCIONES
            self.game.draw_text("Creditos", 40, self.creditsx, self.creditsy) #Tamaño de la opcion  CREDITOS
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False



class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume' #Opcion de "SONIDO"
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        width = 945
        x = 0
        while self.run_display:
            self.game.check_events()
            self.check_input()

            #Imagen de fondo de opcion "Opciones"
            background = pygame.image.load("background3.jpg").convert()
            self.game.display.fill(self.game.BLACK)
            self.game.display.blit(background,(x,0))
            #Poner imagen en loop
            x_relativa = x % background.get_rect().width
            self.game.display.blit(background, (x_relativa - background.get_rect().width, 0))
            if (x_relativa < width):
                self.game.display.blit(background, (x_relativa, 0))
            x -= 5

            self.game.draw_text('Opciones', 60, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 50)
            self.game.draw_text("Sonido", 40, self.volx, self.voly)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
##            if self.state == 'Volume':
##                self.state = 'Controls'
##                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            if self.state == 'Controls': #Opcion de sonido (volume)
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            # TO-DO: Create a Volume Menu and a Controls Menu
            pass

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        width = 945
        x = 0
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False

            #Imagen de fondo de opcion "Creditos"
            background = pygame.image.load("background3.jpg").convert()
            self.game.display.fill(self.game.BLACK)
            self.game.display.blit(background,(x,0))
            #Poner imagen en loop
            x_relativa = x % background.get_rect().width
            self.game.display.blit(background, (x_relativa - background.get_rect().width, 0))
            if (x_relativa < width):
                self.game.display.blit(background, (x_relativa, 0))
            x -= 5

            self.game.draw_text('Creditos', 60, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 50)
            self.game.draw_text('Hecho por', 35, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 20) #Al cambiar el numero final (ejemplo : 20) se modifica la posición de las palabras
            self.game.draw_text('Julieta Miranda', 17, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 70)
            self.game.draw_text('Tamara Pucheta', 17, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 100)
            self.game.draw_text('Lucas Sosa', 17, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 130)
            self.blit_screen()

