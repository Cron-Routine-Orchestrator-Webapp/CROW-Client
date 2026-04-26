from typing import TypedDict


class Request(TypedDict):
    PID: int
    ACTION_TYPE: str
    COMMAND: str
    ARGS: list[str]
    ABSOLUT_PATH: str
    PYTHON_EXE: str


class Response(TypedDict):
    STATUS: str
    CODE: int
    PID: int
    ACTION_TYPE: str
    OUTPUT: str
