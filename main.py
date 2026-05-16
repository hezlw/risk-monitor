from fastapi import FastAPI

from database import cursor

app = FastAPI()

@app.get("/trades")
def get_trades():

    cursor.execute("""

    SELECT *
    FROM trades
    ORDER BY id DESC
    LIMIT 100

    """)

    rows = cursor.fetchall()

    result = []

    for row in rows:

        result.append({

            "id": row[0],
            "symbol": row[1],
            "side": row[2],
            "price": row[3],
            "qty": row[4],
            "amount": row[5],
            "created_at": row[6]
        })

    return result

@app.get("/alerts")
def get_alerts():

    cursor.execute("""

    SELECT *
    FROM alerts
    ORDER BY id DESC
    LIMIT 50

    """)

    rows = cursor.fetchall()

    result = []

    for row in rows:

        result.append({

            "id": row[0],
            "alert_type": row[1],
            "message": row[2],
            "created_at": row[3]
        })

    return result