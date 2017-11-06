'''
This universal_code.py is
    designed and worked by Excelino.Fernando
    improved and added to perfection by Felix.Anggara
'''
import pygame, time, random
from Final_Project.colours_RGB import *
from Final_Project.universal_fonts import *

#game setup
def game_setup_init(set_caption, set_game_icon):
    pygame.display.set_caption(set_caption)
    game_icon = pygame.image.load(set_game_icon)
    pygame.display.set_icon(game_icon)

def initializer(width, height):
#We can put the display_width and display_height into one class and use them as
# the parent class, while the other code from text_display to message_display will
# be inheriting the data from the parent
#It's also necessary to put pygame.init() into the return to get it outside of the function
    display_width = width #Change this to get one wished width screen
    display_height = height #Change this to get one wished height screen
    #icon_pic = pygame.image.load(icon_name)
    #icon = pygame.display.set_icon(icon_pic)
    screenDisplay = pygame.display.set_mode((display_width, display_height), pygame.HWSURFACE, 0)
    screen_Box = screenDisplay.get_rect()
    return pygame.init(), screenDisplay, screen_Box

#------------------------------------------------------------------------------
#text_display(text, font): is used to get the colour, render
# and display the text to screen
#this text_display is also count as tuple, but it is used to get input
# data from user and return the 'tuple'
def text_display(text, font, colour):
    textToSurface = font.render(text, True, colour)
    return textToSurface, textToSurface.get_rect()
#----------------------------------
#This is Text_Align class. It is used for creating the alignment of the text or objects on the game screen
#There are 9 presets, "topLeft", "topCenter", "topRight", "middleLeft", "middleCenter", "middleRight", "bottomLeft",
#"bottomCenter", and "bottomRight"
#The case is insensitive to make the declaration easier
#To use this, first you need to declare Text_Align class into variable.
#After that, you use the alignment method to select the alignment and outputting the coordinate tuple.
#You can use the alignment method multiple times to align different objects and using different presets.
#For example:
#alignit=Text_Align(<name of your screen box>)-->Initial declaration of Text_Align
#alignit.alignment("<one of 9 avaiable presets>")-->Create the alignment boolean
class Text_Align:
    def __init__(self, screen_box):
        self.screen_Box = screen_box
        self.textPosition = 0
    def alignment(self, aligning):
        self.aligning = aligning.lower()
        if self.aligning == "topleft":
            self.text_topLeft()
        elif self.aligning == "topcenter":
            self.text_topCenter()
        elif self.aligning == "topright":
            self.text_topRight()
        elif self.aligning == "middleleft":
            self.text_middleLeft()
        elif self.aligning == "middlecenter":
            self.text_middleCenter()
        elif self.aligning == "middleright":
            self.text_middleRight()
        elif self.aligning == "bottomleft":
            self.text_bottomLeft()
        elif self.aligning == "bottomcenter":
            self.text_bottomCenter()
        elif self.aligning == "bottomright":
            self.text_bottomRight()
        return self.textPosition

#text_positionYpositionX
#text_topLeft(): will make the text position to the topLeft of
#the screen by taking the center of the x-Coordinate screen and divide it by 2
#meanwhile this text_topleft() is the 'pure' tuple, because it is used to
#calculate the data they got from input 'tuple'

    def text_topLeft(self):
        x = self.screen_Box.centerx/2
        y = 30
        self.textPosition = (x) , (y)
        #print(textPosition)

#text_topCenter(): will make the text position to the topCenter of
# the screen by taking the center of the x-Coordinate screen,
# so that the position of the text wil be located in middle and
# after that by making the y-Coordinate to 30,
# it will make the position of the text to the top or exactly 30 from the top of screen
    def text_topCenter(self):
        x = self.screen_Box.centerx
        y = 30
        self.textPosition = (x) , (y)
        #print(textPosition)

#text_topRight(): will make the text position to the topCenter of
# the screen by taking the center of the x-Coordinate screen and times it by 1.5
# or multiplied by 3 and divided by 2,
# so that the position of the text will be located in Right
# and after that by making the y-Coordinate to 30,
# it will make the position of the text to the top or exactly 30 from the top of screen
    def text_topRight(self):
        x = self.screen_Box.centerx*3/2
        y = 30
        self.textPosition = (x) , (y)
        #print(textPosition)

#text_middleLeft(): will make the text position to the middleLeft of
# the screen by taking the center of the x-Coordinate screen and divide it by 2,
# so that the position of the text will be located in Left and
# after that by taking the center of the y-Coordinate of the screen, it will make the position
# of the text to middle
    def text_middleLeft(self):
        x = self.screen_Box.centerx/2
        y = self.screen_Box.centery
        self.textPosition = (x) , (y)
        #print(textPosition)

#text_middleCenter(): will make the text position to the middleCenter of
# the screen by taking the center of the x-Coordinate screen,
# so that the position of the text wil be located in middle
# and after that by taking the center of the y-Coordinate of the screen, it will make the position
# of the text to Center
    def text_middleCenter(self):
        x = self.screen_Box.centerx
        y = self.screen_Box.centery
        self.textPosition = (x) , (y)
        #print(textPosition)

#text_middleRight(): will make the text position to the middleRight of
# the screen by taking the center of the x-Coordinate screen and times it by 1.5
# or multiplied by 3 and divided by 2,
# so that the position of the text will be located in Right
# and after that by taking the center of the y-Coordinate of the screen, it will make the position
# of the text to middle
    def text_middleRight(self):
        x = self.screen_Box.centerx*3/2
        y = self.screen_Box.centery
        self.textPosition = (x) , (y)
        #print(textPosition)

#text_bottomLeft(): will make the text position to the bottomLeft of
# the screen by taking the center of the x-Coordinate screen and divide it by 2,
# so that the position of the text will be located in Left
# and after that by taking the display_height of the screen and subtracted it by 30,
# it will make the position of the text to the bottom or -30 of the assigned display_height
    def text_bottomLeft(self):
        x = self.screen_Box.centerx/2
        y = self.screen_Box.height-30
        self.textPosition = (x) , (y)
        #print(textPosition)

#text_bottomCenter(): will make the text position to the bottomCenter of
# the screen by taking the center of the x-Coordinate screen,
# so that the position of the text will be located in Center
# and after that by taking the display_height of the screen and subtracted it by 30,
# it will make the position of the text to the bottom or -30 of the assigned display_height
    def text_bottomCenter(self):
        x = self.screen_Box.centerx
        y = self.screen_Box.height-30
        self.textPosition = (x) , (y)
        #print(textPosition)

#text_bottomRight(): will make the text position to the bottomRight of
# the screen by taking the center of the x-Coordinate screen and times it by 1.5
# or multiplied by 3 and divided by 2,
# so that the position of the text will be located in Right
# and after that by taking the display_height of the screen and subtracted it by 30,
# it will make the position of the text to the bottom or -30 of the assigned display_height
    def text_bottomRight(self):
        x = self.screen_Box.centerx*3/2
        y = self.screen_Box.height-30
        self.textPosition = (x) , (y)
        #print(textPosition)

#message_display(input_text, font_name, font_size, font_colour, font_position)
# this message_display is used to display a message or inputted text on the screen
# with the pre-defined position, there're 9 positions which you can use
# e.g. text_bottomLeft to make the text into bottom and Left side
def message_display(screen, input_text, font_name, font_size, font_colour, font_position):
    textFont = pygame.font.Font(font_name, font_size)
    textSurf, textRect = text_display(input_text, textFont, font_colour)
    textRect.center = (font_position)
    screen.blit(textSurf, textRect)

#def message_displayXY(input_text, font_name, font_size, font_colour,
#                     font_positionX, font_positionY):
# this message_displayXY is used to display a message or inputted text with the
# defined X-coordinate and Y-coordinate to define the position of the text on the screen
def message_displayXY(screen,input_text, font_name, font_size, font_colour,
                      font_positionX, font_positionY):
    textFont = pygame.font.Font(font_name, font_size)
    textSurf, textRect = text_display(input_text, textFont, font_colour)
    textRect.center = ((font_positionX), (font_positionY))
    screen.blit(textSurf, textRect)

def image_display(screen,input_image,resizing_image,image_width,
                  image_height,image_position):
    imageSurf = pygame.image.load(input_image)
    if resizing_image:
        imageSurf = pygame.transform.scale(imageSurf, (image_width,image_height))
    imageRect = imageSurf.get_rect()
    imageRect.center = (image_position)
    screen.blit(imageSurf, imageRect)

def image_displayXY(screen,input_image,resizing_image,image_width,
                    image_height,image_positionX,image_positionY):
    imageSurf = pygame.image.load(input_image)
    if resizing_image:
        imageSurf = pygame.transform.scale(imageSurf, (image_width,image_height))
    imageRect = imageSurf.get_rect()
    imageRect.center = ((image_positionX),(image_positionY))
    screen.blit(imageSurf, imageRect)

def buttonXY(screen, input_text, text_colour, button_positionX, button_positionY, button_width,
             button_height, inactive_colour, active_colour, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)

    if button_positionX+button_width > mouse[0] > button_positionX \
            and button_positionY+button_height > mouse[1] > button_positionY:
        pygame.draw.rect(screen, active_colour,(button_positionX, button_positionY,
                                                button_width, button_height))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, inactive_colour,(button_positionX, button_positionY,
                                                  button_width, button_height))

    textFont = pygame.font.Font(font_LemonMilk(), 20)
    textSurf, textRect = text_display(input_text, textFont, text_colour)
    textRect.center = ((button_positionX+(button_width/2), (button_positionY+(button_height/2))))
    screen.blit(textSurf, textRect)


#This is an example of how you will use the universal_codes.py and
#how it will work...
#----------------------------------example----------------------------------------
initial,screenDisplay,screen_Box= initializer(800, 400)
def example():
    align = Text_Align(screen_Box)
    clock = pygame.time.Clock()
    intro = True
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        print(screen_Box[2]) #X
        print(screen_Box[3]) #Y
        screenDisplay.fill(White)
        #image_display(screenDisplay,'x.bmp',False,0,0,align.alignment("middlecenter"))
        #image_displayXY(screenDisplay,'y.png',False,0,0,60,60)
        #message_display(screenDisplay, 'print at topLeft', font_LemonMilk(), 30, colour_Black(), align.alignment("topLeft"))
        #message_display(screenDisplay,'topLeft', font_LemonMilk(), 30, colour_Maroon(), align.alignment("topleft"))
        #message_display(screenDisplay,'topCenter', font_LemonMilk(), 30, colour_Aqua(), align.alignment("topcenter"))
        #message_display(screenDisplay,'topRight', font_LemonMilk(), 30, colour_Green(), align.alignment("topright"))
        #message_display(screenDisplay,'middleLeft', font_LemonMilk(), 30, colour_Teal(), align.alignment("middleleft"))
        #message_display('Main Menu', font_LemonMilk(), 30, font_middleCenter())
        #message_display(screenDisplay,'middleRight', font_LemonMilk(), 30, colour_Olive(), align.alignment("middleright"))
        #message_display(screenDisplay,'bottomLeft', font_LemonMilk(), 30, colour_Silver(), align.alignment("bottomleft"))
        #message_display(screenDisplay,'bottomCenter', font_LemonMilk(), 30, colour_Purple(), align.alignment("bottomcenter"))
        #message_display(screenDisplay,'bottomRight', font_LemonMilk(), 30, Lime, align.alignment("bottomRight"))
        #message_displayXY(screenDisplay,'displayXY', font_AlexxisDemo(), 50, Navy, 600, 300)
        pygame.display.update()
        clock.tick(15) #15FPS
#example
#----------------------------------example----------------------------------------
