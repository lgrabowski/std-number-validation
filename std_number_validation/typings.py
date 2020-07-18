import typing
from std_number_validation import algorithms

BaseAlgorithmType = typing.TypeVar('BaseAlgorithmType', bound=algorithms.BaseAlgorithm)