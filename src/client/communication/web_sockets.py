import asyncio
from websockets.asyncio.server import serve


class WebSocketsServer:
    def __init__(self) -> None:
        pass

    async def hello(self, websocket) -> None:
        name: str = await websocket.recv()
        print(f"<<< {name}")

        greeting: str = f"Hello {name}!"

        await websocket.send(greeting)
        print(f">>> {greeting}")

    async def testing(self) -> None:
        async with serve(self.hello, "localhost", 5000) as server:
            await server.serve_forever()


if __name__ == "__main__":
    server = WebSocketsServer()
    asyncio.run(server.testing())
