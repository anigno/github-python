import sqlite3

conn = sqlite3.connect('d:\\temp\\example.db')
c = conn.cursor()

c.execute("create table if not exists Dictionary (key text, value text)")
c.execute("INSERT INTO Dictionary VALUES ('Name','Roni')")
a=c.execute("SELECT * FROM Dictionary")
for b in a:
    print(b)


w