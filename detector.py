from database import cursor

THRESHOLD = 100000

def detect_large_trade():

    cursor.execute("""

    SELECT *
    FROM trades
    ORDER BY id DESC
    LIMIT 20

    """)

    rows = cursor.fetchall()

    for row in rows:

        amount = row[5]

        if amount > THRESHOLD:

            print(
                f"⚠ 大额异常成交: "
                f"${amount:,.2f}"
            )

if __name__ == "__main__":

    detect_large_trade()