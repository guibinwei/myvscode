#claude改进版-pygame

import pygame
import random
import pyttsx3
import sqlite3
import atexit

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gold Coin Game")
clock = pygame.time.Clock()

engine = pyttsx3.init()
engine.setProperty('rate', 140)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

conn = sqlite3.connect('goldcoin.db')
cur = conn.cursor()

def cleanup():
    global conn, cur
    try:
        if cur:
            cur.close()
        if conn:
            conn.close()
    except sqlite3.ProgrammingError:
        pass  # Ignore the error if the database is already closed
    finally:
        pygame.quit()

atexit.register(cleanup)

class Actor:
    def __init__(self, image):
        self.image = pygame.image.load(f"images/{image}.png").convert_alpha()
        self.rect = self.image.get_rect()

    def draw(self):
        screen.blit(self.image, self.rect)

    def collidepoint(self, pos):
        return self.rect.collidepoint(pos)

alien = Actor('alien')
alien.rect.x = 300
alien.rect.y = 200

alien2 = Actor('alien2')
alien2.rect.x = 500
alien2.rect.y = 200

gems = []
gems2 = []

def query_database(name):
    sql_count = f"SELECT COUNT(*) FROM scores WHERE name='{name}'"
    sql_sum = f"SELECT SUM(number) FROM scores WHERE name='{name}'"
    sql_all = f"SELECT * FROM scores WHERE name='{name}'"
    
    cur.execute(sql_count)
    count = cur.fetchone()[0]
    
    cur.execute(sql_sum)
    total = cur.fetchone()[0]
    
    cur.execute(sql_all)
    records = cur.fetchall()
    
    return count, total, records

def create_gems(actor, records):
    gems = []
    for i, record in enumerate(records):
        gem = Actor('gemgreen')
        gem.rect.x = actor.rect.x + (i % 5) * 40 - 80
        gem.rect.y = actor.rect.y + 150 + (i // 5) * 40
        gem.record = record
        gems.append(gem)
    return gems

def set_alien_hurt():
    global gems
    alien.image = pygame.image.load("images/alien_hurt.png").convert_alpha()
    count, total, records = query_database('shiya')
    words = f"I am Shiya, I have received rewards {count} times, with a total of {total} gold coins."
    engine.say(words)
    engine.runAndWait()
    gems = create_gems(alien, records)
    pygame.time.set_timer(pygame.USEREVENT, 5000)  # Set timer for 5 seconds

def set_alien2_hurt():
    global gems2
    alien2.image = pygame.image.load("images/alien2_hurt.png").convert_alpha()
    count, total, records = query_database('shiqi')
    words = f"I am Shiqi, I have received rewards {count} times, with a total of {total} gold coins."
    engine.say(words)
    engine.runAndWait()
    gems2 = create_gems(alien2, records)
    pygame.time.set_timer(pygame.USEREVENT + 1, 5000)  # Set timer for 5 seconds

def set_gem_hurt(gem):
    gem.image = pygame.image.load("images/gem_hurt.png").convert_alpha()
    date, number, reason = gem.record[2], gem.record[1], gem.record[3]
    words = f"This gold coin was earned on {date}, because {reason}, and received a reward of {number} gold coins."
    engine.say(words)
    engine.runAndWait()
    pygame.time.set_timer(pygame.USEREVENT + 2, 5000)  # Set timer for 5 seconds

def set_alien_normal():
    alien.image = pygame.image.load("images/alien.png").convert_alpha()

def set_alien2_normal():
    alien2.image = pygame.image.load("images/alien2.png").convert_alpha()

def set_gem_normal(gem):
    gem.image = pygame.image.load("images/gemgreen.png").convert_alpha()

running = True
try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if alien.collidepoint(pos):
                    set_alien_hurt()
                elif alien2.collidepoint(pos):
                    set_alien2_hurt()
                else:
                    for gem in gems + gems2:
                        if gem.collidepoint(pos):
                            set_gem_hurt(gem)
            elif event.type == pygame.USEREVENT:
                set_alien_normal()
            elif event.type == pygame.USEREVENT + 1:
                set_alien2_normal()
            elif event.type == pygame.USEREVENT + 2:
                for gem in gems + gems2:
                    set_gem_normal(gem)

        screen.fill((80, 0, 70))
        alien.draw()
        alien2.draw()
        for gem in gems + gems2:
            gem.draw()

        pygame.display.flip()
        clock.tick(60)
finally:
    cleanup()
