from .base_validator import BaseValidator


class BooleanValidator(BaseValidator):
    """
    Validator implementation which returns boolean or raises exception
    """

    def determine_output(self, value) -> bool:
        """
        Shorthand function to check of bool should be return or exception thrown
        :param value:
        :return:
        """
        if self.exception is None:
            return value
        else:
            raise self.exception
