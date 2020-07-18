# entry point
import typing

from std_number_validation import exceptions
from std_number_validation import algorithms
from std_number_validation import validation
from std_number_validation import typings

def validate(number: int,
             algorithm: typing.Type[typings.BaseAlgorithm]=algorithms.LuhnAlgorithm,
             exc_to_raise=None) -> validation.BooleanValidator:
    """

    :param exc_to_raise:
    :param number:
    :param algorithm:
    :return:
    """
    return validation.BooleanValidator(number, algorithm, exc_to_raise)


def context_validation(number: int,
             algorithm: typing.Type[typings.BaseAlgorithm]=algorithms.LuhnAlgorithm,
             exc_to_raise=None) -> validation.ContextValidator:
    """

    :param exc_to_raise:
    :param number:
    :param algorithm:
    :return:
    """
    return validation.ContextValidator(number, algorithm, exc_to_raise)


