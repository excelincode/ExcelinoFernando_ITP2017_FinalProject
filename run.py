from Final_Project.main import *
from Final_Project.universal_codes_01 import *
from pygame import *

def run():
    initializer(800, 600)
    display.set_caption("Contraflow: Act Alpha!")

    final_score = 0
    score = 0

    FPS = pygame.time.Clock()
    game_time = pygame.time.get_ticks()
    init_time = pygame.time.get_ticks()

    Menu_FPS = 20
    Game_FPS = 45
    pygame.init()

    ambulance_all = Ambulance()
    player_car = Group(ambulance_all)

    obstacle_group = Group()

    running = True
    while running:
        FPS(Game_FPS)
        Game_FPS += 0.1



