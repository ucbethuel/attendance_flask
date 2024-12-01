import sqlite3

db_name = "concept.db"

conn = sqlite3.connect(":memory:")

cursor = conn.cursor()


cursor.execute("""
CREATE TABLE attendance (
               id integer,
               name text,
               rank text)
""")

conn.commit()
conn.execute(""" INSERT INTO attendance VALUES (4, "Benedicta", "Hi") """)
print(conn.execute(""" SELECT name FROM attendance """).fetchall())
conn.total_changes
print()

conn.commit()
conn.close()
