import asyncio
import json
import time
import websockets

from database import conn, cursor

SYMBOL = "btcusdt"

async def main():

    url = f"wss://stream.binance.com:9443/ws/{SYMBOL}@aggTrade"

    print("正在连接 Binance WebSocket...")

    async with websockets.connect(url) as ws:

        print("✅ WebSocket 已连接")

        while True:

            message = await ws.recv()

            data = json.loads(message)

            price = float(data['p'])
            qty = float(data['q'])

            maker = data['m']

            side = "SELL" if maker else "BUY"

            amount = price * qty

            created_at = int(time.time())

            print(
                f"{side} | "
                f"price={price} | "
                f"qty={qty}"
            )

            cursor.execute("""

            INSERT INTO trades
            (
                symbol,
                side,
                price,
                qty,
                amount,
                created_at
            )

            VALUES (?, ?, ?, ?, ?, ?)

            """, (
                SYMBOL,
                side,
                price,
                qty,
                amount,
                created_at
            ))

            conn.commit()

asyncio.run(main())