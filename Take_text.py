#!/usr/bin/env python

"""

/*******************************************************
 * Copyright 2026 Vintets <programmer@vintets.ru> - All Rights Reserved
 * Written by Vintets <programmer@vintets.ru>, June 2026
*******************************************************/

# for python 3.12.0 and over
"""

__version_info__ = ('1', '0', '0')
__version__ = '.'.join(__version_info__)
__author__ = 'master by Vint'
__title__ = '--- Take_text ---'
__copyright__ = 'Copyright 2026 (c)  bitbucket.org/Vintets'


# import os
from pathlib import Path
import sys

from accessory import authorship, check_version, exit_from_program, init_console, logger
import errors as err
import pyperclip


ALLOWED_TYPES = ('.txt', '.md', '.svg', '.html', '.css', '.js', '.py', '.ini', '.cmd', '.bat')


def get_transferred_argument() -> str:
    try:
        arg = sys.argv[1]
    except IndexError:
        raise err.ArgumentNotPassedError()  # from None
    return arg


def validate_transferred_argument(arg: str) -> Path:
    file_in = Path(arg)
    if not file_in.exists():
        raise err.FileNotExistError(str(file_in))
    elif not file_in.is_file():
        raise err.ArgumentIsFolderError()
    elif file_in.suffix not in ALLOWED_TYPES:
        raise err.FileTypeNotAllowedError(str(file_in), ALLOWED_TYPES)
    return file_in


def read_text_file(filename: Path) -> str:
    with open(filename, 'r', encoding='utf-8') as fr:
        data = fr.read()
    return data


def main() -> None:
    pyperclip.copy('')
    arg = get_transferred_argument()
    filename = validate_transferred_argument(arg)
    text_data = read_text_file(filename)
    pyperclip.copy(text_data)
    print(text_data)


if __name__ == '__main__':
    init_console(width=120, hight=50)
    check_version(version=(3, 12, 0))
    # PATH_SCRIPT = Path(__file__).parent
    # os.chdir(PATH_SCRIPT)

    authorship(__author__, __title__, __version__, __copyright__)  # width=_width

    try:
        main()
    except KeyboardInterrupt:
        logger.info('Отмена. Скрипт остановлен.')
        exit_from_program(code=0)
    except (err.ArgumentNotPassedError,
            err.FileNotExistError,
            err.FileTypeNotAllowedError,
            ) as e:
        logger.error(e)
        err.process_critical_exception()
    except Exception as e:
        logger.critical(e)  # __str__()
        # raise e
        err.process_critical_exception()

    exit_from_program(code=0, close=True)
