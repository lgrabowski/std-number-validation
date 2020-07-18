import typing
from std_number_validation import typings


class BaseValidator:

    def __init__(self, number: int, algorithm: typing.Type[typings.BaseAlgorithmType], exc_to_raise: Exception):
        pass