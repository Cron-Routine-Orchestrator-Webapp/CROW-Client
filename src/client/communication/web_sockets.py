import asyncio
from websockets.asyncio.server import serve
from ..exec_handling.executor import Executor
from ..helper.types import Request, Response


class WebSocketsServer:
    def __init__(self) -> None:
        self.executor = Executor()

    async def hello(self, websocket) -> None:
        name: str = await websocket.recv()
        print(f"<<< {name}")

        greeting: str = f"Hello {name}!"

        await websocket.send(greeting)
        print(f">>> {greeting}")

    async def work(self, websocket) -> None:
        package: Request = await websocket.recv()
        print(f"received: {package}")

        try:
            output = self.executor.parsing(package)
            status, code = "success", 200
        except Exception as e:
            output = str(e)
            status, code = "error", 500

        response: Response = {
            "STATUS": status,
            "CODE": code,
            "PID": package["PID"],
            "ACTION_TYPE": package["ACTION_TYPE"],
            "OUTPUT": output,
        }

        await websocket.send(response)
        print(f"sended: {response}")

    async def run(self) -> None:
        async with serve(self.work, "localhost", 5000) as server:
            await server.serve_forever()


if __name__ == "__main__":
    server = WebSocketsServer()
    asyncio.run(server.run())
