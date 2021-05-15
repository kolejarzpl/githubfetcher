import sqlite3

conn = sqlite3.connect('user.db')

c = conn.cursor()

#c.execute("""CREATE TABLE users (
 #           first text,
  #          last text,
   #         pay integer
    #        )""")

c.execute("INSERT INTO users VALUES ('NICKes','ID',1000)")
#powyżej będzie nasz URL (albo CSV)

c.execute("SELECT * FROM users WHERE last ='ID'")

print(c.fetchall())

conn.commit()

conn.close()