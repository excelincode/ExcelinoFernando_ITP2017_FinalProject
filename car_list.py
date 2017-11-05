import pygame, time, random
from Final_Project.colours_RGB import *
from Final_Project.universal_fonts import *

# ---------------------------------------------------------
car_EdgarLVL1_image = "Sprites/Ambulance.png"
car_EdgarLVL1_image_crashed = "Sprites/Mini_Van.png"
car_EdgarLVL1_speed = (-10, 10, 5, -5)
class P1_Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_P1_Car = pygame.image.load(car_EdgarLVL1_image)
        self.rect = self.image.get_rect()

    # move mole to a new random location when it gets hit
    def speed(self):
        acceleration = car_EdgarLVL1_speed[0]#y up or K_UP
        deacceleration = car_EdgarLVL1_speed[1]#y down or K_DOWN
        agile_right = car_EdgarLVL1_speed[2]#x left or K_Left
        agile_left = car_EdgarLVL1_speed[3]#x right or K_right
        return acceleration, deacceleration, agile_right, agile_left

    def crash_target(self, hit_target):
        self.image_P1_Car = pygame.image.load(car_EdgarLVL1_image_crashed)
        return self.rect.colliderect(hit_target)

    def update(self, pt):
        self.image = pygame.image.load("Animated_Pistol1.png")
        self.rect.center = pt

    def draw(self, screen):
        screen.blit(self.image_P1_Car, self.rect)
class Volks_wagons(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Sprites/Car.png").convert_alpha()
        self.rect = self.image.get_rect()

    # move Volks_wagon to a new random location when it gets hit
    def flee(self):
        x = random.randint(0, display_width-1-self.rect.width)
        y = random.randint(0, display_height-1-self.rect.height)
        self.rect.topleft = (x,y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
# -----------------------------------

def centerImage(screen, im):
    x = (scrWidth - im.get_width() - 10)
    y = (scrHeight - im.get_height())
    screen.blit(im, (x, 0))

# ---------- main -------------
background_image = 'Backgrounds/Road_Texture.jpg'
pygame.init()

display_width = 1200 #Change this to get one wished width screen
display_height = 600 #Change this to get one wished height screen
screenDisplay = pygame.display.set_mode((display_width, display_height))
screen_Box = screenDisplay.get_rect()
screenDisplay.fill(colour_Black())
pygame.display.set_caption("Contraflow: Police Chase Act#1")
background = pygame.image.load(background_image).convert()

#hide the mouse cursor
pygame.mouse.set_visible(False)

font = pygame.font.Font(None, 40)

hitSnd = pygame.mixer.Sound('Sounds/BG_Sounds/Ambulance.wav')
hitSnd.set_volume(1)

# create sprites and a group
P_car = P1_Car
random_car = Volks_wagons

# game vars
hits = 0
mousePos = (display_width/2, display_height/2)
DELAY = 800
clock = pygame.time.Clock()


running = True
while running:
    clock.tick(30)

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        if event.type == MOUSEMOTION:
            mousePos = pygame.mouse.get_pos()
        if event.type == MOUSEBUTTONDOWN:
            running = True

    # update game
    shovel.update(mousePos)
    ev = pygame.event.wait()
    if ev.type == pygame.QUIT:
        pygame.quit()
        break
    elif ev.type == pygame.K_DOWN:
        if P_car.hit(random_car):
            hitSnd.play()
            P_car.
            hits += 1

            pygame.time.set_timer(USEREVENT + 1, DELAY)
        else:
            hitSnd.play()
    elif ev.type == USEREVENT + 1:
        mole.flee()


    # redraw game
    screen.blit(background, (0, 0))
    mole.draw(screen)
    shovel.draw(screen)

    # time elapsed (in secs)
    time = int(pygame.time.get_ticks()/1000)
    timeIm = font.render(str(time), True, colour_Green())
    screen.blit(timeIm, (10,10))

    hitIm = font.render("Hits = " + str(hits), True, colour_Maroon())
    centerImage(screen, hitIm)

    pygame.display.update()
