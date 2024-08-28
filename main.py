from game import Game


g = Game()


while g.running: #Mientras comience el programa comienza :
    g.curr_menu.display_menu() #Menu principal
    g.game_loop() # Juego principal
