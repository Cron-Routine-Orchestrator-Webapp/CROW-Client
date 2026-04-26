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

    async def work(self, websocket):
        package: Request = await websocket.recv()
        print(f"received: {package}")

        try:
            output: str = self.executor.parsing(package)
            response: Response = {
                "STATUS": "success",
                "CODE": 200,
                "PID": package["PID"],
                "ACTION_TYPE": package["ACTION_TYPE"],
                "OUTPUT": output,
            }
        except Exception as e:
            response: Response = {
                "STATUS": "error",
                "CODE": 500,
                "PID": package["PID"],
                "ACTION_TYPE": package["ACTION_TYPE"],
                "OUTPUT": str(e),
            }

        await websocket.send(response)
        print(f"sended: {response}")

    async def testing(self) -> None:
        async with serve(self.work, "localhost", 5000) as server:
            await server.serve_forever()


if __name__ == "__main__":
    server = WebSocketsServer()
    asyncio.run(server.testing())
