import sqlite3
conn = sqlite3.connect('test-2023-10-24-3.db')
cur = conn.cursor()
# 建表的sql语句 
sql_text_1 = '''CREATE TABLE scores5 
           (姓名 TEXT, 
            班级 TEXT, 
            性别 TEXT, 
            语文 NUMBER, 
            数学 NUMBER, 
            英语 NUMBER);''' 
# 执行sql语句 
cur.execute(sql_text_1)

# 插入单条数据 
sql_text_2 = "INSERT INTO scores5 VALUES('A2', '一班', '男', 96, 94, 98)" 
cur.execute(sql_text_2)

data = [('B2', '一班', '女', 78, 87, 85), 
        ('C2', '一班', '男', 98, 84, 90), 
        ] 
cur.executemany('INSERT INTO scores5 VALUES (?,?,?,?,?,?)', data) 
# 连接完数据库并不会自动提交，所以需要手动 commit 你的改动conn.commit()


# 查询数学成绩大于90分的学生 
sql_text_3 = "SELECT * FROM scores5 WHERE 数学>90" 
cur.execute(sql_text_3) 
# 获取查询结果 
rs=cur.fetchall()
print (rs)

# 提交改动的方法 
conn.commit()
#在python代码中没有提交，结果数据是空的，所以下述的select返回也是空的，后来在Jupyter中分段演示，发现问题


# 关闭游标 
cur.close() 
# 关闭连接 
conn.close()


