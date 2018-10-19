##I'm Manachanok Sirivibulkovit  6001012630101
##This project is a chart of random number when you click a 'RANDOM' button
## my blog : http://manachanok94.blogspot.com

import pygame, sys
from pygame.locals import *
import random

    #Set Display
pygame.init() #
pygame.display.init()
pygame.display.get_surface()
size = width, height = (410, 550)

    # Set colors
gray = (230, 230, 230)
white = (238, 238, 238)
orange = (255, 225, 140)
black = (60, 60, 60)

bsize = bwidth, bheight = (100,60)
margin = 2 #The margin between each cell

grid = []
# Loop for each row
for row in range(10) :# For each row , create a list that will represent an entire row
    grid.append([])
    # Loop for each column
    for column in range(10): # Add a number to the current row
        grid[row].append(0)

#Set font
font = pygame.font.SysFont("Segoe UI", 22)

screen = pygame.display.set_mode(size)
bg = pygame.Surface(screen.get_size())
bg.convert()
bg.fill(gray)

textlist = [x for x in range(1, 29)]

state = False
while not state:
    pygame.display.set_caption('Random')
    screen.blit(bg, (0, 0))
    screen.set_at((1, 1), black)

    for event in pygame.event.get():  # When user do something...
        if event.type == pygame.QUIT:  # If user click for close the window will close
            done = True
            quit()
        if pygame.mouse.get_pressed()[0] == 1: #Random list of number
            pos = pygame.mouse.get_pos()
            if 150 < pos[0] < 129 + 150 and 460 < pos[1] < 460 + 60:
                textlist = random.sample(range(1, 29), 28)

    if pygame.mouse.get_pressed()[0] == 1: #Change color
        pos = pygame.mouse.get_pos()
        if 150 < pos[0] < 129 + 150 and 460 < pos[1] < 460 + 60:
            pygame.draw.rect(screen, white, (129, 460, 150, 60))
    else:
        pygame.draw.rect(screen, orange, (129, 460, 150, 60))

    r_pos = (129 + (70 / 2)), (460 + (30 / 2))
    r_str = font.render('RANDOM', True, black)
    screen.blit(r_str, r_pos)
    #print(textlist)
    i = 0
    for row in range(7):
        for column in range(4):
            column_click = column
            row_click = row
            if row <= 1:
                color = white
            #pygame.draw.rect(screen, color, (x,y,width,height), thickness)
            button = pygame.draw.rect(screen,
                             color,
                             [(margin + bwidth) * column + margin,
                              (margin + bheight) * row + margin,
                              bwidth,
                              bheight])

            position = ((margin + bwidth) * column + (bwidth / 2.2), (margin + bheight) * row + (bheight / 3.5))

            if row >= 0:# Show text on rect
                text = font.render(str(textlist[i]), True, black)
                screen.blit(text, position)
                i += 1

    pygame.display.update() #
    pygame.display.flip() #If you does not have this code, display will not flip the graphic
pygame.quit() #Help when click to close the window