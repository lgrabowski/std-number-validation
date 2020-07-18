import typing
from std_number_validation import algorithms
from std_number_validation import exceptions

BaseAlgorithmType = typing.TypeVar('BaseAlgorithmType', bound=algorithms.BaseAlgorithm)
BaseExceptionType = typing.TypeVar('BaseExceptionType', bound=exceptions.BaseValidationError)