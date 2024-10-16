#claude改进版-pgzrun

import pgzrun
import random
import pyttsx3
import sqlite3
import atexit

WIDTH = 800
HEIGHT = 600

engine = pyttsx3.init()
engine.setProperty('rate', 140)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

conn = sqlite3.connect('goldcoin.db')
cur = conn.cursor()

def cleanup():
    if conn:
        cur.close()
        conn.close()

atexit.register(cleanup)

alien = Actor('alien')
alien.x = 300
alien.y = 200

alien2 = Actor('alien2')
alien2.x = 500
alien2.y = 200

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
        gem.x = actor.x + (i % 5) * 40 - 80
        gem.y = actor.y + 150 + (i // 5) * 40
        gem.record = record
        gems.append(gem)
    return gems

def on_mouse_down(pos):
    global gems, gems2
    if alien.collidepoint(pos):
        set_alien_hurt()
    elif alien2.collidepoint(pos):
        set_alien2_hurt()
    else:
        for gem in gems + gems2:
            if gem.collidepoint(pos):
                set_gem_hurt(gem)

def set_alien_hurt():
    global gems
    alien.image = 'alien_hurt'
    count, total, records = query_database('shiya')
    words = f"I am Shiya, I have received rewards {count} times, with a total of {total} gold coins."
    engine.say(words)
    engine.runAndWait()
    gems = create_gems(alien, records)
    clock.schedule_unique(set_alien_normal, 5.0)

def set_alien2_hurt():
    global gems2
    alien2.image = 'alien2_hurt'
    count, total, records = query_database('shiqi')
    words = f"I am Shiqi, I have received rewards {count} times, with a total of {total} gold coins."
    engine.say(words)
    engine.runAndWait()
    gems2 = create_gems(alien2, records)
    clock.schedule_unique(set_alien2_normal, 5.0)

def set_gem_hurt(gem):
    gem.image = 'gem_hurt'
    date, number, reason = gem.record[2], gem.record[1], gem.record[3]
    words = f"This gold coin was earned on {date}, because {reason}, and received a reward of {number} gold coins."
    engine.say(words)
    engine.runAndWait()
    clock.schedule_unique(lambda: set_gem_normal(gem), 5.0)

def set_alien_normal():
    alien.image = 'alien'

def set_alien2_normal():
    alien2.image = 'alien2'

def set_gem_normal(gem):
    gem.image = 'gemgreen'

def draw():
    screen.fill((80, 0, 70))
    alien.draw()
    alien2.draw()
    for gem in gems + gems2:
        gem.draw()

pgzrun.go()
