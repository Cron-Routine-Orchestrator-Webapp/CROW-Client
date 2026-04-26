import subprocess
from ..helper.types import Request


class Executor:
    def __init__(self) -> None:
        pass

    def parsing(self, package: Request) -> str:
        match package["ACTION_TYPE"]:
            case "cmd":
                return self.execute_cmd(package["COMMAND"], *package["ARGS"])
            case "shell_cmd":
                return self.execute_shell_cmd(package["COMMAND"])
            case "python_file":
                return self.execute_python_file(
                    package["ABSOLUT_PATH"], package["PYTHON_EXE"]
                )
            case _:
                raise ValueError(
                    f"{package['ACTION_TYPE']} is not a valid action type."
                )

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
        output: subprocess.CompletedProcess[str] = subprocess.run(
            [python_exe, absolute_path], text=True
        )
        print(
            f"The python file '{absolute_path}' ran in the python exe '{python_exe}' with output '{output.stdout}'"
        )
        return output.stdout
