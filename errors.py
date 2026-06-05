import os
from typing import Optional

from accessory import cprint


def process_critical_exception(message: Optional[str] = None) -> None:
    """Prints message, describing critical situation, and exit"""

    if message is not None:
        print(message)
    cprint('14{dash}   ^12_ERROR   ^14_{dash}'.format(dash='-' * 20))
    os._exit(1)


class ArgumentNotPassedError(Exception):
    """Error argument not passed (file csv)."""
    def __init__(self) -> None:
        self.msg = f'Не передан файл для обработки!'

    def __str__(self) -> str:
        return self.msg


class ArgumentIsFolderError(Exception):
    """Error argument is folder."""
    def __init__(self) -> None:
        self.msg = f'Передана директория, а не файл!'

    def __str__(self) -> str:
        return self.msg


class FileNotExistError(Exception):
    """Error argument file not exist."""
    def __init__(self, file_in: str):
        super().__init__(file_in)
        self.msg = f"Файл '{file_in}' не существует!"

    def __str__(self) -> str:
        return self.msg


class FileTypeNotAllowedError(Exception):
    """Error file type not allowed."""
    def __init__(self, file_in: str, allowed_types: tuple) -> None:
        super().__init__(file_in, allowed_types)
        self.msg = f"Передан файл неразрешённого формата! '{file_in}'\nРазрешённые форматы: {allowed_types}"

    def __str__(self) -> str:
        return self.msg
