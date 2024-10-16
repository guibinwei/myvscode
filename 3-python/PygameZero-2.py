alien = Actor("alien")
alien.topright = 400, 200

WIDTH = 500
HEIGHT = alien.height + 200


def draw():
    screen.clear()
    alien.draw()

def update():
    alien.left += 0.5
    if alien.left > WIDTH:
        alien.right = 0

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()


def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 1.0)

def set_alien_normal():
    alien.image = 'alien'