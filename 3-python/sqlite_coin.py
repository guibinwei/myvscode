import sqlite3
conn = sqlite3.connect('goldcoin.db')
cur = conn.cursor()
# 建表的sql语句 
sql_text_1 = '''CREATE TABLE scores 
           (姓名 TEXT, 
            日期 TEXT, 
            数量 NUMBER, 
            原因 TEXT);''' 
# 执行sql语句 
cur.execute(sql_text_1)

data = [('贵诗雅', '10月24日星期二', 1, '写英文字母得到的'), 
        ('贵诗雅', '10月26日星期四', 1, '数学同步练还差一题，但是爸爸可怜我，给我一个金币'), 
        ('贵诗淇', '10月26日星期四', 1, '把数学同步练做完得到的'), 
        ] 
cur.executemany('INSERT INTO scores VALUES (?,?,?,?)', data) 
# 连接完数据库并不会自动提交，所以需要手动 commit 你的改动conn.commit()

# 提交改动的方法 
conn.commit()
#在python代码中没有提交，结果数据是空的，所以下述的select返回也是空的，后来在Jupyter中分段演示，发现问题


# 关闭游标 
cur.close() 
# 关闭连接 
conn.close()


