import pgzrun
import random

TITLE = 'Flappy Bird'
WIDTH = 400
HEIGHT = 708

# These constants control the difficulty of the game
GAP = 130
GRAVITY = 0.3
FLAP_STRENGTH = 6.5
SPEED = 3

bird = Actor('bird1', (10, 10))
bird.dead = False
bird.score = 0
bird.vy = 0

pipe_top = Actor('top', anchor=('left', 'bottom'), pos=(40, 100))
pipe_bottom = Actor('bottom', anchor=('left', 'top'), pos=(40, 200))

def draw():
    screen.clear()
    bird.draw()
    pipe_top.draw()
    pipe_bottom.draw()