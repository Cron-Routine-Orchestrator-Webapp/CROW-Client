from pydantic import BaseModel


class Request(BaseModel):
    PID: int
    ACTION_TYPE: str
    COMMAND: str | None
    ARGS: list[str] | None
    ABSOLUT_PATH: str | None
    PYTHON_EXE: str | None


class Response(BaseModel):
    STATUS: str
    CODE: int
    PID: int
    ACTION_TYPE: str
    OUTPUT: str | None
