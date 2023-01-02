import os
import typing
from pathlib import Path

from envparse import env as _raw

T = typing.TypeVar('T')


def load(file_path: str):
    path = Path(file_path)
    _raw.read_envfile(path)


def parse(var_name: str, default=..., cast_func=lambda x: x):
    if var_name in os.environ:
        return cast_func(os.environ[var_name])
    if default is ...:
        raise ValueError(f'Environment variable "{var_name}" not set')
    return default


class Env:
    def __init__(self, file_path: str):
        load(file_path)

    @staticmethod
    def get(var_name: str, default: T = ...) -> str | T:
        return parse(var_name, default)

    @staticmethod
    def get_int(var_name: str, default: T = ...) -> int | T:
        return parse(var_name, default, int)

    @staticmethod
    def get_list(var_name: str, default: T = ...) -> list | T:
        return parse(var_name, default, lambda x: x.split(','))


env = Env('.env')
