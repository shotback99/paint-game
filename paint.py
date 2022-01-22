"""
Press 'r' to close the program.
You can edit the LENGTH and WIDTH variables to match your screen size
"""

import pygame as p # Allows us to use the module pygame :)
import random
#Initialises pygame
p.init()

LENGTH = 1950
WIDTH = 1200

P_WIDTH = 10
P_LENGTH = 10

plr_colour = [100, 100, 100] # RGB
bg_colour = (180, 90, 70)

title = "Super cool game"
game_loop = True

plr_speed = 20
n = 0

screen = p.display.set_mode((LENGTH, WIDTH))

player = p.Rect(P_WIDTH - 20, P_LENGTH/2, 50, 50)# assigns the coordinates and size of player

p.display.set_caption(title)

def window():
    #screen.fill(bg_colour)
    p.draw.rect(screen, plr_colour, player) # draws player onto screen
    p.display.flip()
    if player.x <= 0: # adds constraints to the player, so they don't go out of bounds
        player.x += plr_speed
    if player.x >= LENGTH:
        player.x -= plr_speed
    if player.y <= 0:
        player.y += plr_speed
    if player.y >= WIDTH:
        player.y -= plr_speed


def animation(): # this is what makes it move randomly
    ans = random.randint(1, 4)
    if ans == 1: player.x -= plr_speed
    elif ans == 2: player.y -= plr_speed
    elif ans == 3: player.y += plr_speed
    else: player.x += plr_speed

while game_loop: # Updates the window

    for event in p.event.get():
        if event.type == p.QUIT:
            game_loop = False

    keys = p.key.get_pressed() # dictionary of current inputs, True if activated

    if keys[p.K_a]:#list: contains multiple variables
        player.x -= plr_speed
    if keys[p.K_d]:
        player.x += plr_speed
    if keys[p.K_w]:
        player.y -= plr_speed
    if keys[p.K_s]:
        player.y += plr_speed
    if keys[p.K_r]:
        game_loop = False
    if plr_colour[n] <= 255:
        plr_colour[n] += 0.5
    else:
        plr_colour[n] = 100
        n+= 1
        if n == 3: n = 0

    window() # displays window
    animation() # comment this entire line out if you just want to move the player without the animation

p.quit()
