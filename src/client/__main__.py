import asyncio
from communication.web_sockets import WebSocketsServer


def main() -> None:
    try:
        server = WebSocketsServer()
        print("Startup successful!")
        asyncio.run(server.run())
    except KeyboardInterrupt:
        print("\n Programm terminated by user.")


if __name__ == "__main__":
    main()
