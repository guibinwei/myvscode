import pgzrun
import random
import pyttsx3
import sqlite3

WIDTH = 800
HEIGHT = 600

engine = pyttsx3.init()  # 创建对象
engine.setProperty('rate', 140)
engine.setProperty('volume', 1.0)  # 设置新的语音音量，音量最小为 0，最大为 1
#可以更大
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 设置声音

conn = sqlite3.connect('goldcoin.db')
cur = conn.cursor()
#查询诗雅
sql_text_1 ='''
SELECT SUM(number) AS "total"  
FROM scores  
WHERE name=='贵诗雅'; '''

sql_text_2 = "SELECT * FROM scores WHERE name=='贵诗雅' "

cur.execute(sql_text_1) 
# 获取查询结果 
rs1=cur.fetchall()
print (rs1)

cur.execute(sql_text_2) 
# 获取查询结果 
rs2=cur.fetchall()
print (rs2)
words = "我是小萌可"+"我有"+str(rs1[0][0])+"个金币。"
print (words)
i=1
words1 = "这是我的第"+str(rs2[i-1][1])+"个金币"+rs2[i-1][2]+ rs2[i-1][3]
print (words1)
words2 = """我是中小学生，
我有两个金币。"""
words21 = """这个金币是我星期二写英文字母得到的。"""

alien = Actor('alien')
alien.x = 300
alien.y = 200

alien2 = Actor('alien2')
alien2.x = 500
alien2.y = 200

gem = Actor('gemgreen')
gem.x = alien.x
gem.y = alien.y+150

#score = 0
#game_over = False
alien.dead = False
alien.score = 0

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()
    if gem.collidepoint(pos):
        set_gem_hurt()
    if alien2.collidepoint(pos):
        set_alien2_hurt()


def set_alien_hurt():
    alien.image = 'alien_hurt'
    #sounds.eep.play()
    engine.say(words)
    engine.runAndWait()
    engine.stop()
    clock.schedule_unique(set_alien_normal, 5.0)

def set_alien_normal():
    alien.image = 'alien'

def set_alien2_hurt():
    alien2.image = 'alien2_hurt'
    #sounds.eep.play()
    engine.say(words2)
    engine.runAndWait()
    engine.stop()
    clock.schedule_unique(set_alien2_normal, 5.0)

def set_alien2_normal():
    alien2.image = 'alien2_hurt'
    
def set_gem_hurt():
    gem.image = 'gem_hurt'
    #sounds.eep.play()
    engine.say(words1)
    engine.runAndWait()
    engine.stop()
    clock.schedule_unique(set_gem_normal, 5.0)
    
def set_gem_normal():
    gem.image = 'gemgreen'
    
def draw():
    screen.fill((80,0,70))
    gem.draw()
    alien.draw()
    alien2.draw()


cur.close() 
# 关闭连接 
conn.close()
pgzrun.go() # Must be last line