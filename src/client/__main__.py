import asyncio
from communication.web_sockets import WebSocketsServer

def main() -> None:
    server = WebSocketsServer()
    asyncio.run(server.run())

if __name__ == "__main__":
    main()