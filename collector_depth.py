import asyncio
import json
import websockets

SYMBOL = "btcusdt"

async def main():

    url = f"wss://stream.binance.com:9443/ws/{SYMBOL}@depth"

    print("正在连接 OrderBook...")

    async with websockets.connect(url) as ws:

        print("✅ OrderBook 已连接")

        while True:

            message = await ws.recv()

            data = json.loads(message)

            bids = data['b']
            asks = data['a']

            print("\n========== ORDER BOOK ==========")

            print("\nBUY BIDS:")

            for bid in bids[:5]:

                print(
                    f"price={bid[0]} "
                    f"qty={bid[1]}"
                )

            print("\nSELL ASKS:")

            for ask in asks[:5]:

                print(
                    f"price={ask[0]} "
                    f"qty={ask[1]}"
                )

asyncio.run(main())