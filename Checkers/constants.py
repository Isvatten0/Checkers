import pygame
import random

WIDTH = 800
HEIGHT = 800
ROWS = 8
COLS = 8
SQUARE_SIZE = WIDTH//COLS

RED = (158, 27, 50)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GRAY = (162, 170, 173)

# Generate a random number between 0 and 255
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
r2 = random.randint(0, 255)
g2 = random.randint(0, 255)
b2 = random.randint(0, 255)
r3 = random.randint(0, 255)
g3 = random.randint(0, 255)
b3 = random.randint(0, 255)
r4 = random.randint(0, 255)
g4 = random.randint(0, 255)
b4 = random.randint(0, 255)

# Create a tuple of the random RGB values
FUNCOLOR = (r, g, b)
FUNCOLOR2 = (r2, g2, b2)
FUNCOLOR3 = (r3, g3, b3)
FUNCOLOR4 = (r4, g4, b4)

LIGHTBLUE = (173, 216, 230)