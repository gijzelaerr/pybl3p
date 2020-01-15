import asyncio
import json
import websockets
from pybl3p.public import trades_stream


async def pybl3p_loop():
    async for msg in trades_stream():
        print(msg)


async def other_loop():
    url = "wss://ws.bitstamp.net."
    async with websockets.connect(url) as websocket:
        payload = {
            "event": "bts:subscribe",
            "data": {
                "channel": "live_trades_btceur"
            }
        }
        await websocket.send(payload)
        async for message in websocket:
            yield json.loads(message)


async def main():
    loops = {pybl3p_loop(), other_loop()}
    await asyncio.wait(loops)


if __name__ == '__main__':
    asyncio.run(main())
