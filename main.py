import os, sys
from pygame import *
from pygame.sprite import *


from Final_Project.universal_fonts import *
from Final_Project.colours_RGB import *
from Final_Project.universal_codes import *

#Global Variable
display_width = 720
display_height = 720
pause = False

FPS = pygame.time.Clock()
Menu_FPS = 20

initial, screenDisplay, screen_Box= initializer(display_width, display_height)
align = Text_Align(screen_Box)

#saving the score into a save folder with score_save.dat which will be used to
#saving the topScore and becomes the database for it
zero = 0
if not os.path.exists("save/score_save.dat"):
    f=open("save/score_save.dat",'w')
    f.write(str(zero))
    f.close()
v=open("save/score_save.dat",'r')
topScore = int(v.readline())
v.close()

def scoreboard(screen, data, x, y, input_text_colour, input_font,
            input_font_size, input_message_format = 'Dodged: %d'):
    #display the score
    font = pygame.font.Font(input_font, input_font_size)
    text = font.render(input_message_format%data, True, input_text_colour)
    screen.blit(text, (x, y))


def load_image(x , y, image_name):
    img = pygame.image.load(image_name)
    screenDisplay.blit(img, (x, y))

def quit_game():
    pygame.quit()
    quit()

def game_unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False

def game_pause():
    global pause, align, FPS, Menu_FPS
    ############
    pygame.mixer.music.pause()
    #############
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #screenDisplay.fill(White)
        message_display(screenDisplay, "Pause!", font_LemonMilk(), 100,
                        Red, align.alignment("middleCenter"))
        buttonXY(screenDisplay, "Continue!", Black, display_width*0.3,
                 display_height*0.7, 300, 50, Green, Lime, game_unpause)
        buttonXY(screenDisplay, "Quit!", Black, display_width*0.3,
                 display_height*0.8, 300, 50, Maroon, Red, quit_game)


        pygame.display.update()
        FPS.tick(Menu_FPS)

def game_intro():
    global pause, align, FPS, Menu_FPS, screenDisplay, screen_Box
    pygame.mixer.music.load("Sounds/BG_Musics/atlanta.wav")
    pygame.mixer.music.play(-1)

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screenDisplay.fill(White)

        message_display(screenDisplay, "Contraflow: Act Alpha!", font_EclipseDemo(), 42, Black,
                        align.alignment("middleCenter"))

        buttonXY(screenDisplay, "Play!", Black, display_width*0.45, display_height*0.7, 100, 50, Green, Lime, game_run)
        buttonXY(screenDisplay, "Quit!", Black, display_width*0.45, display_height*0.8, 100, 50, Maroon, Red, quit_game)

        pygame.display.update()
        FPS.tick(Menu_FPS)

def crash():
    crash_sound = pygame.mixer.Sound("Sounds/BG_Sounds/crash.wav")
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()

    message_displayXY(screenDisplay, "CRASHED!", font_AnotherDanger(), 90, Red, display_width/2, display_height/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        buttonXY(screenDisplay, "Play!", Black, display_width*0.45, display_height*0.7, 100, 50, Green, Lime, game_run)
        buttonXY(screenDisplay, "Quit!", Black, display_width*0.45, display_height*0.8, 100, 50, Maroon, Red, quit_game)

        pygame.display.update()


def game_run():
    global pause, topScore, display_width, display_height
    score = 0
    pygame.mixer.music.load('Sounds/BG_Musics/Deja_Vu.wav')
    pygame.mixer.music.play(-1)

    x_player_location = (display_width * 0.45)
    y_player_location = (display_height * 0.7)

    x_change = 0


    ambulance_width = 102*0.9
    ambulance_height = 207*0.9

    obstacle_width = 118*0.9
    obstacle_height = 226*0.9

    x_left_dangerZone = 120
    x_right_dangerZone = 530
    obstacle_startX = random.randrange(x_left_dangerZone, x_right_dangerZone)
    obstacle_startY = -600
    obstacle_speed = 4

    road_startY = 800

    BG_speed = 3

    game_time = pygame.time.get_ticks()

    Game_FPS = 60
    game_stop = False
    while not game_stop:
        #to get the time passed in game by dividing it with 1000 which is going to
        #convert the 1000ms to 1 second
        time_pass = (pygame.time.get_ticks() - game_time)/1000

        for event in pygame.event.get():
            pygame.display.flip()
            key_Pressed = pygame.key.get_pressed()
            pygame.display.flip()
            if event.type == pygame.QUIT or key_Pressed[K_ESCAPE]:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_p:
                    pause = True
                    game_pause()
            if key_Pressed[K_LEFT]:
                load_image(x_player_location, y_player_location, 'Sprites/ambulance_animation/3.png')
                x_change = -5
                pygame.display.flip()
            if key_Pressed[K_RIGHT]:
                load_image(x_player_location, y_player_location, 'Sprites/ambulance_animation/1.png')
                x_change = 5
                pygame.display.flip()
        x_player_location += x_change
        screenDisplay.fill(White)

        load_image(0, road_startY, 'Backgrounds/Road_Fix.jpg')
        load_image(obstacle_startX, obstacle_startY, 'Sprites/Fake_Taxi.png')
        load_image(x_player_location, y_player_location, 'Sprites/ambulance_animation/2.png')

        #playing sound will causing a drastic drop in FPS, so it's wiseful to not to play it
        #sound = pygame.mixer.Sound("Sounds/BG_Sounds/Ambulance.wav")
        #pygame.mixer.Sound.play(sound)
        #pygame.mixer.Sound.set_volume(sound, -1)

        obstacle_startY += obstacle_speed
        ambulance_speed = obstacle_speed*Game_FPS
        road_startY += BG_speed

        scoreboard(screenDisplay, topScore, 20, 25,
                   Red, font_LemonMilk(), 20, 'Top Score: %d')
        scoreboard(screenDisplay, ambulance_speed, 20, 50,
                   White, font_LemonMilk(), 20, 'Speed: %d FPS')
        scoreboard(screenDisplay, score, 20, 75,
                   Blue, font_LemonMilk(), 20, 'Current Score: %d')
        scoreboard(screenDisplay, time_pass, display_width-200, 25,
                   Green, font_LemonMilk(), 20, 'Time: %d')
        if x_player_location > 530 or x_player_location < 120:
            crash()

        #if obstacle is passing the display_height it will respawn the new one
        if obstacle_startY > display_height:
            obstacle_startY = 0 - display_height
            obstacle_startX = random.randrange(x_left_dangerZone, x_right_dangerZone)
            score += 1
            obstacle_speed += 1

        #reset Background back to repeat it again
        if road_startY > -1:
            road_startY = -500

        #checking coalision with area_x_left, area_x_right and obstacles
        if y_player_location < (obstacle_startY + obstacle_height) \
        and y_player_location + ambulance_height >= obstacle_startY:
            if x_player_location > obstacle_startX \
            and x_player_location < (obstacle_startX + obstacle_width) \
            or x_player_location + ambulance_width > obstacle_startX \
            and x_player_location + ambulance_width < obstacle_startX + obstacle_width:
                crash()

        #will save the score to the topScore if higher
        if score > topScore:
            file=open("save/score_save.dat",'w')
            file.write(str(score))
            file.close()
            topScore = score

        pygame.display.update()
        FPS.tick(Game_FPS)

#Reference to pygame.org, pygame.net
#Reference to SentDex, https://pythonprogramming.net/pygame-python-3-part-1-intro/
#Special thanks to Georgius, Felix
