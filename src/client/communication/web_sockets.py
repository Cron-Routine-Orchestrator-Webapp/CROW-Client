import asyncio
from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed

from client.exec_handling.executor import Executor
from client.helper.types import Request, Response


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
        try:
            async for data in websocket:
                try:
                    # Parse request safely
                    package = Request.model_validate_json(data)
                    print(f"received: {package}")

                    # Execute command
                    try:
                        output = self.executor.parsing(package)
                        status, code = "success", 200
                    except Exception as e:
                        output = str(e)
                        status, code = "error", 500

                    # Build response
                    response = Response(
                        STATUS=status,
                        CODE=code,
                        PID=package.PID,
                        ACTION_TYPE=package.ACTION_TYPE,
                        OUTPUT=output,
                    )

                    # Send safely (connection might die anytime)
                    try:
                        await websocket.send(response.model_dump_json())
                        print(f"sent: {response}")
                    except ConnectionClosed:
                        print("Client disconnected while sending response")
                        return

                except Exception as e:
                    print(f"Invalid request: {e}")

        except ConnectionClosed:
            print("Connection closed")

    async def run(self) -> None:
        async with serve(self.work, "localhost", 5000) as server:
            await server.serve_forever()


if __name__ == "__main__":
    server = WebSocketsServer()
    asyncio.run(server.run())
