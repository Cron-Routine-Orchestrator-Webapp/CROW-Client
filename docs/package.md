# Package-Guide

This document describes the exact package format for requests as well as for answers as a python data-class whit additional informations.

## request

```python
from typing import TypedDict

class Request(TypedDict):
    PID: int
    ACTION_TYPE: str
    COMMAND: str
    ARGS: list[str]
    ABSOLUT_PATH: str
    PYTHON_EXE: str
```

### Table

| Key              | Type        | Options                                                                       | Optional | Notes                                 |
| :--------------- | :---------- | :---------------------------------------------------------------------------- | :------- | :------------------------------------ |
| `"PID"`          | `int`       | `100`-`999`                                                                   | `False`  |                                       |
| `"ACTION_TYPE"`  | `str`       | `"cmd"`, `"shell_cmd"`, `"python_file"`                                       | `False`  |                                       |
| `"COMMAND"`      | `str`       | eg. `"apt upgrade"`                                                           | `True`   | Only nedded for `cmd` and `shell_cmd` |
| `"ARGS"`         | `list[str]` | eg. `["-y"]`                                                                  | `True`   | Only nedded for `cmd`                 |
| `"ABSOLUT_PATH"` | `str`       | eg. `"/home/user/backup/backup.py"`                                           | `True`   | Only nedded for `pyhton_file`         |
| `"PYTHON_EXE"`   | `str`       | eg. `"/home/user/backup/.env/bin/python"` OR `None` for system default python | `True`   | Only nedded for `pyhton_file`         |
