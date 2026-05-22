import subprocess
from ..helper.types import Request


class Executor:
    def __init__(self) -> None:
        pass

    def parsing(self, package: Request) -> str:
        match package.ACTION_TYPE:
            case "cmd":
                command: str | None = package.COMMAND
                args: list[str] = package.ARGS or []
                if command is None:
                    raise KeyError("COMMAND is required for action type 'cmd'")
                return self.execute_cmd(command, *args)
            case "shell_cmd":
                command = package.COMMAND
                if command is None:
                    raise KeyError("COMMAND is required for action type 'shell_cmd'")
                return self.execute_shell_cmd(command)
            case "python_file":
                absolute_path: str | None = package.ABSOLUT_PATH
                python_exe: str = package.PYTHON_EXE or "python"
                if absolute_path is None:
                    raise KeyError(
                        "ABSOLUT_PATH is required for action type 'python_file'"
                    )
                return self.execute_python_file(absolute_path, python_exe)
            case _:
                raise ValueError(f"{package.ACTION_TYPE} is not a valid action type.")

    def execute_cmd(self, command: str, *arguments: str) -> str:
        output: subprocess.CompletedProcess[str] = subprocess.run(
            [command, *arguments], capture_output=True, text=True
        )
        print(f"The command '{command}' ran with output '{output.stdout}'")
        return output.stdout

    def execute_shell_cmd(self, command: str) -> str:
        output: subprocess.CompletedProcess[str] = subprocess.run(
            command, shell=True, text=True
        )
        print(f"The command '{command}' ran with output '{output.stdout}'")
        return output.stdout

    def execute_python_file(
        self, absolute_path: str, python_exe: str = "python"
    ) -> str:
        if python_exe is None:
            python_exe = "python"
        output: subprocess.CompletedProcess[str] = subprocess.run(
            [python_exe, absolute_path], text=True
        )
        print(
            f"The python file '{absolute_path}' ran in the python exe '{python_exe}' with output '{output.stdout}'"
        )
        return output.stdout
