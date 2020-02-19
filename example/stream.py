import asyncio
import json
import websockets
from pybl3p.public import trades_stream


async def pybl3p_loop():
    async for msg in trades_stream():
        print(f"bl3p: {msg}")


async def bitstamp_loop():
    bitstamp_subscribe = {
        "event": "bts:subscribe",
        "data": {
            "channel": "live_trades_btceur"
        }
    }

    bitstamp_url = "wss://ws.bitstamp.net"

    async def other_loop():
        async with websockets.connect(bitstamp_url) as websocket:
            await websocket.send(json.dumps(bitstamp_subscribe))
            async for message in websocket:
                yield json.loads(message)

    async for msg in other_loop():
        print(f"bitstamp: {msg}")


async def main():
    loops = {pybl3p_loop(), bitstamp_loop()}
    await asyncio.wait(loops)


if __name__ == '__main__':
    asyncio.run(main())
