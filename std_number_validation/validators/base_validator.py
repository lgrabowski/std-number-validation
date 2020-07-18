import typing
from std_number_validation import typings


class BaseValidator:

    def __init__(self, number: int,
                 algorithm: typing.Type[typings.BaseAlgorithmType],
                 exc_to_raise: typing.Type[typings.BaseExceptionType] = None):
        self.param = number
        self.algorithm = algorithm()
        self.exception = exc_to_raise

    def parameter_validation(self, param) -> bool:
        """
        Since we are valid mostly number we expect this methid to be common
        across all validators.
        :param param:
        :return:
        """
        return isinstance(param, int)

    def is_valid(self) -> bool:
        """
        Attaches main public interface with algorithms execution
        controls flow (return bool or raise an exception according to configuration)
        :return:
        """
        if self.parameter_validation(self.param):
            if self.algorithm.is_valid(self.param):
                return True
            else:
                return self.determine_output(False)
        else:
            return self.determine_output(False)

    def determine_output(self, validation_result) -> bool:
        """
        default behaviour to process output
        :param validation_result:
        :return:
        """
        return validation_result
