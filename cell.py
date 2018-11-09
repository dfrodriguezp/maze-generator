from setup import *
import numpy
import pygame
pygame.init()

class Cell(object):
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.walls = [True, True, True, True] # Top, right, bottom, left
        self.visited = False
    
    def checkNeighbors(self, mesh):
        neighbors = list()
        dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        for i, j in dirs:
            i_ = self.i + i
            j_ = self.j + j
            if (i_ > -1) and (j_ > -1) and (i_ < cols) and (j_ < rows):
                nhb = mesh[i_][j_]
                if not nhb.visited:
                    neighbors.append(nhb)

        if len(neighbors) > 0:
            return numpy.random.choice(neighbors)
        else:
            return None

    def show(self):
        x = self.i * w
        y = self.j * w
        if self.visited:
            pygame.draw.rect(canvas, orange, (x+1.5, y+1.5, w, w))
    
        if self.walls[0]:
            pygame.draw.line(canvas, blue, (x, y), (x+w, y), 3)
        if self.walls[1]:
            pygame.draw.line(canvas, blue, (x+w, y), (x+w, y+w), 3)
        if self.walls[2]:
            pygame.draw.line(canvas, blue, (x, y+w), (x+w, y+w), 3)
        if self.walls[3]:
            pygame.draw.line(canvas, blue, (x, y), (x, y+w), 3)
        
    def highlight(self):
        x = self.i*w
        y = self.j*w
        pygame.draw.rect(canvas, yellow, (x+1.5, y+1.5, w-1.5, w-1.5))