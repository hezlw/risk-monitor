from database import cursor

from alert_service import save_alert

WINDOW = 20

def detect_wash():

    cursor.execute("""

    SELECT side, price, amount
    FROM trades
    ORDER BY id DESC
    LIMIT ?

    """, (WINDOW,))

    rows = cursor.fetchall()

    alternating = 0

    for i in range(len(rows) - 1):

        side1 = rows[i][0]
        side2 = rows[i + 1][0]

        amount1 = rows[i][2]
        amount2 = rows[i + 1][2]

        if side1 != side2:

            diff = abs(amount1 - amount2)

            if diff < 100:

                alternating += 1

    if alternating >= 10:

        msg = "Possible Wash Trading"

        print(f"⚠ {msg}")

        save_alert(
            "WASH_TRADING",
            msg
        )

if __name__ == "__main__":

    detect_wash()