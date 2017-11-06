from Final_Project.main import *
from pygame import *

def run():
    game_setup_init('Contraflow: Act Alpha!', 'icon.png')
    game_intro()
    game_run()
    pygame.quit()
    quit()
run()
