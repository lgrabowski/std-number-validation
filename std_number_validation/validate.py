# entry point
import typing

from std_number_validation import algorithms
from std_number_validation import validators
from std_number_validation import typings


def validation(number: int,
               algorithm: typing.Type[typings.BaseAlgorithmType] = algorithms.LuhnAlgorithm,
               exc_to_raise=None) -> validators.BooleanValidator:
    """

    :param exc_to_raise:
    :param number:
    :param algorithm:
    :return:
    """
    return validators.BooleanValidator(number, algorithm, exc_to_raise)


def contextual_validation(number: int,
                          algorithm: typing.Type[typings.BaseAlgorithmType] = algorithms.LuhnAlgorithm,
                          exc_to_raise=None) -> validators.ContextValidator:
    """

    :param exc_to_raise:
    :param number:
    :param algorithm:
    :return:
    """
    return validators.ContextValidator(number, algorithm, exc_to_raise)
