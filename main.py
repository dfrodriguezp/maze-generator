from setup import *
from cell import *
import sys
import numpy
import pygame
pygame.init()

def setup():
	pass

def draw():
	pass
# Setup
grid = [[None for j in range(rows)] for i in range(cols)]
clock = pygame.time.Clock()

for i in range(cols):
    for j in range(rows):
        grid[i][j] = Cell(i, j)

current = grid[0][0]
stack = list()

# Draw
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    canvas.fill(purple)
    for i in range(cols):
        for j in range(rows):
            grid[i][j].show()

    current.visited = True
    current.highlight()
    nxt = current.checkNeighbors(grid)
    if nxt:
        nxt.visited = True
        stack.append(current)
        removeWalls(current, nxt)
        current = nxt

    elif len(stack) > 0:
        current = stack.pop()

    pygame.display.update()
    clock.tick(30)
