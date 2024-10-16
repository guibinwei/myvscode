alien = Actor('alien')
alien.pos = 100, 56

WIDTH = 500
HEIGHT = alien.height + 200

def draw():
    screen.clear()
    alien.draw()