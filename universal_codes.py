'''
This code is open-source and for educational purpose only.
Note that every code is linked with one and other modules.

This universal_code is
    designed and worked by Excelino.Fernando
'''

import pygame, time, random
from Final_Project.colours_RGB import *
from Final_Project.universal_fonts import *

pygame.init() #It's also necessary to put pygame.init() into the parent class
#Can we put the display_width and display_height into one class and use them as
# the parent class, while the other code from text_display to message_display will
# be inheriting the data from the parent, can we?
display_width = 1200 #Change this to get one wished width screen
display_height = 600 #Change this to get one wished height screen

screenDisplay = pygame.display.set_mode((display_width, display_height))
screen_Box = screenDisplay.get_rect()
#------------------------------------------------------------------------------
#text_display(text, font): is used to get the colour, render
# and display the text to screen
#this text_display is also count as tuple, but it is used to get input
# data from user and return the 'tuple'
def text_display(text, font, colour):
    textToSurface = font.render(text, True, colour)
    return textToSurface, textToSurface.get_rect()
#----------------------------------
'''
text_positionYpositionX
text_topLeft(): will make the text position to the topLeft of
the screen by taking the center of the x-Coordinate screen and divide it by 2
meanwhile this text_topleft() is the 'pure' tuple, because it is used to
calculate the data they got from input 'tuple'
'''
def text_topLeft():
    x = screen_Box.centerx/2
    y = 30
    textPosition = (x) , (y)
    #print(textPosition)
    return textPosition

#text_topCenter(): will make the text position to the topCenter of
# the screen by taking the center of the x-Coordinate screen,
# so that the position of the text wil be located in middle and
# after that by making the y-Coordinate to 30,
# it will make the position of the text to the top or exactly 30 from the top of screen
def text_topCenter():
    x = screen_Box.centerx
    y = 30
    textPosition = (x) , (y)
    #print(textPosition)
    return textPosition

#text_topRight(): will make the text position to the topCenter of
# the screen by taking the center of the x-Coordinate screen and times it by 1.5
# or multiplied by 3 and divided by 2,
# so that the position of the text will be located in Right
# and after that by making the y-Coordinate to 30,
# it will make the position of the text to the top or exactly 30 from the top of screen
def text_topRight():
    x = screen_Box.centerx*3/2
    y = 30
    textPosition = (x) , (y)
    #print(textPosition)
    return textPosition

#text_middleLeft(): will make the text position to the middleLeft of
# the screen by taking the center of the x-Coordinate screen and divide it by 2,
# so that the position of the text will be located in Left and
# after that by taking the center of the y-Coordinate of the screen, it will make the position
# of the text to middle
def text_middleLeft():
    x = screen_Box.centerx/2
    y = screen_Box.centery
    textPosition = (x) , (y)
    #print(textPosition)
    return textPosition

#text_middleLeft(): will make the text position to the middleLeft of
# the screen by taking the center of the x-Coordinate screen,
# so that the position of the text wil be located in middle
# and after that by taking the center of the y-Coordinate of the screen, it will make the position
# of the text to Center
def text_middleCenter():
    x = screen_Box.centerx
    y = screen_Box.centery
    textPosition = (x) , (y)
    #print(textPosition)
    return textPosition

#text_middleRight(): will make the text position to the middleRight of
# the screen by taking the center of the x-Coordinate screen and times it by 1.5
# or multiplied by 3 and divided by 2,
# so that the position of the text will be located in Right
# and after that by taking the center of the y-Coordinate of the screen, it will make the position
# of the text to middle
def text_middleRight():
    x = screen_Box.centerx*3/2
    y = screen_Box.centery
    textPosition = (x) , (y)
    #print(textPosition)
    return textPosition

#text_bottomLeft(): will make the text position to the bottomLeft of
# the screen by taking the center of the x-Coordinate screen and divide it by 2,
# so that the position of the text will be located in Left
# and after that by taking the display_height of the screen and subtracted it by 30,
# it will make the position of the text to the bottom or -30 of the assigned display_height
def text_bottomLeft():
    x = screen_Box.centerx/2
    y = display_height-30
    textPosition = (x) , (y)
    #print(textPosition)
    return textPosition

#text_bottomCenter(): will make the text position to the bottomCenter of
# the screen by taking the center of the x-Coordinate screen,
# so that the position of the text will be located in Center
# and after that by taking the display_height of the screen and subtracted it by 30,
# it will make the position of the text to the bottom or -30 of the assigned display_height
def text_bottomCenter():
    x = screen_Box.centerx
    y = display_height-30
    textPosition = (x) , (y)
    #print(textPosition)
    return textPosition

#text_bottomCenter(): will make the text position to the bottomCenter of
# the screen by taking the center of the x-Coordinate screen and times it by 1.5
# or multiplied by 3 and divided by 2,
# so that the position of the text will be located in Right
# and after that by taking the display_height of the screen and subtracted it by 30,
# it will make the position of the text to the bottom or -30 of the assigned display_height
def text_bottomRight():
    x = screen_Box.centerx*3/2
    y = display_height-30
    textPosition = (x) , (y)
    #print(textPosition)
    return textPosition

#message_display(input_text, font_name, font_size, font_colour, font_position)
# this message_display is used to display a message or inputted text on the screen
# with the pre-defined position, there're 9 positions which you can use
# e.g. text_bottomLeft to make the text into bottom and Left side
def message_display(input_text, font_name, font_size, font_colour, font_position):
    textFont = pygame.font.Font(font_name, font_size)
    textSurf, textRect = text_display(input_text, textFont, font_colour)
    textRect.center = (font_position)
    screenDisplay.blit(textSurf, textRect)

#def message_displayXY(input_text, font_name, font_size, font_colour,
#                     font_positionX, font_positionY):
# this message_displayXY is used to display a message or inputted text with the
# defined X-coordinate and Y-coordinate to define the position of the text on the screen
def message_displayXY(input_text, font_name, font_size, font_colour,
                      font_positionX, font_positionY):
    textFont = pygame.font.Font(font_name, font_size)
    textSurf, textRect = text_display(input_text, textFont, font_colour)
    textRect.center = ((font_positionX), (font_positionY))
    screenDisplay.blit(textSurf, textRect)

#----------------------------------example----------------------------------------

def game_intro():
    clock = pygame.time.Clock()
    intro = True
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screenDisplay.fill(colour_White())
        message_display('topLeft', font_EclipseDemo(), 60, colour_Black(), text_topLeft())
        message_display('topCenter', font_AnotherDanger(), 30, colour_Black(), text_topCenter())
        message_display('topRight', font_LemonMilk(), 30, colour_Green(), text_topRight())
        message_display('middleLeft', font_LemonMilk(), 30, colour_Teal(), text_middleLeft())
        #message_display('Main Menu', font_LemonMilk(), 30, font_middleCenter())
        message_display('middleRight', font_LemonMilk(), 30, colour_Olive(), text_middleRight())
        message_display('bottomLeft', font_LemonMilk(), 30, colour_Silver(), text_bottomLeft())
        message_display('bottomCenter', font_LemonMilk(), 30, colour_Purple(), text_bottomCenter())
        message_display('bottomRight', font_LemonMilk(), 30, colour_Lime(), text_bottomRight())
        message_displayXY('displayXY', font_AlexxisDemo(), 50, colour_Navy(), 600, 300)

        pygame.display.update()
        clock.tick(15) #15FPS
game_intro()
#----------------------------------example----------------------------------------
