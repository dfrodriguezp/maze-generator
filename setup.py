import pygame
pygame.init()

size = width, height = 600, 600
w = 10
canvas = pygame.display.set_mode(size)
cols = int(width / w)
rows = int(height / w)

black = (0, 0, 0)
white = (255, 255, 255)
grey = (51, 51, 51)
orange = (210, 180, 33)
purple = (53, 0, 110)
blue = (0, 133, 180)
yellow = (255, 255, 0)

def removeWalls(a, b):
    x = a.i - b.i
    if x == 1:
        a.walls[3] = False
        b.walls[1] = False
    elif x == -1:
        a.walls[1] = False
        b.walls[3] = False

    y = a.j - b.j
    if y == 1:
        a.walls[0] = False
        b.walls[2] = False
    elif y == -1:
        a.walls[2] = False
        b.walls[0] = False
