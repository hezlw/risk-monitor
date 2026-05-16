import sqlite3

conn = sqlite3.connect("trades.db")

cursor = conn.cursor()

# trades 表
cursor.execute("""

CREATE TABLE IF NOT EXISTS trades (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    symbol TEXT,
    side TEXT,

    price REAL,
    qty REAL,
    amount REAL,

    created_at INTEGER
)

""")

# alerts 表
cursor.execute("""

CREATE TABLE IF NOT EXISTS alerts (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    alert_type TEXT,

    message TEXT,

    created_at INTEGER
)

""")

conn.commit()

conn.close()

print("✅ 数据库初始化成功")