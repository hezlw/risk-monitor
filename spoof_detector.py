import asyncio
import json
import time
import websockets

SYMBOL = "btcusdt"

large_orders = {}

THRESHOLD = 5

async def main():

    url = f"wss://stream.binance.com:9443/ws/{SYMBOL}@depth"

    async with websockets.connect(url) as ws:

        print("✅ Spoof Detector Running")

        while True:

            message = await ws.recv()

            data = json.loads(message)

            bids = data['b']

            current_prices = set()

            for bid in bids:

                price = bid[0]
                qty = float(bid[1])

                current_prices.add(price)

                # 大额挂单
                if qty > THRESHOLD:

                    if price not in large_orders:

                        large_orders[price] = time.time()

                        print(
                            f"🚨 Large Bid: "
                            f"{price} qty={qty}"
                        )

            # 检查是否快速消失
            remove_list = []

            for price, t in large_orders.items():

                if price not in current_prices:

                    duration = time.time() - t

                    if duration < 5:

                        print(
                            f"⚠ Possible Spoofing: "
                            f"{price}"
                        )

                    remove_list.append(price)

            for price in remove_list:

                del large_orders[price]

asyncio.run(main())