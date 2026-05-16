from database import cursor

cursor.execute("""

SELECT *
FROM trades
ORDER BY id DESC
LIMIT 10

""")

rows = cursor.fetchall()

for row in rows:
    print(row)