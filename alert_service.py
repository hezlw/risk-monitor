import time

from database import conn, cursor

def save_alert(alert_type, message):

    cursor.execute("""

    INSERT INTO alerts
    (
        alert_type,
        message,
        created_at
    )

    VALUES (?, ?, ?)

    """, (

        alert_type,
        message,
        int(time.time())
    ))

    conn.commit()