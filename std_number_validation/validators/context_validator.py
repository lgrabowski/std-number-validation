from .base_validator import BaseValidator


class ContextValidator(BaseValidator):
    """
    Contextual validators for better validators flow
    to have control over exception which may come around param processing from integration
    point of view
    """

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

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
