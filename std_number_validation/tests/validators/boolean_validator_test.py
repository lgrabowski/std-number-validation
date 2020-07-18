import unittest

from std_number_validation import validators
from std_number_validation import algorithms
from std_number_validation import exceptions

class LuhnAlgorithmTestCase(unittest.TestCase):

    BOOLEAN_VALIDATOR_CLASS = validators.BooleanValidator
    LUHN_ALGORITHM = algorithms.LuhnAlgorithm
    CORRECT_NUMBER = 4532015112830366
    INCORRECT_NUMBER = 4532015112830311

    def setUp(self) -> None:
        pass

    def test_checks_if_bool_validator_accepts_valid_number(self):
        """
        BoolValidator should accept correct number
        """
        # given
        validator = self.BOOLEAN_VALIDATOR_CLASS(self.CORRECT_NUMBER, algorithm=self.LUHN_ALGORITHM)
        # when
        is_valid = validator.is_valid()
        # then
        self.assertTrue(is_valid)

    def test_checks_if_bool_validator_rejects_invalid_number(self):
        """
        BoolValidator should reject invalid number
        """
        # given
        validator = self.BOOLEAN_VALIDATOR_CLASS(self.INCORRECT_NUMBER, algorithm=self.LUHN_ALGORITHM)
        # when
        is_valid = validator.is_valid()
        # then
        self.assertFalse(is_valid)

    def test_checks_if_bool_validator_rejects_invalid_param(self):
        """
        BoolValidator should reject invalid param
        """
        # given
        invalid_param = "invalid_param_bazzzzingaaa"  # we check it despsite type checks... this is no java.
        validator = self.BOOLEAN_VALIDATOR_CLASS(invalid_param, algorithm=self.LUHN_ALGORITHM)
        # when
        is_valid = validator.is_valid()
        # then
        self.assertFalse(is_valid)

    def test_checks_if_bool_validator_rejects_invalid_number_and_raises_exception(self):
        """
        BoolValidator should reject invalid number
        """
        # given
        validator = self.BOOLEAN_VALIDATOR_CLASS(self.INCORRECT_NUMBER,
                                                 algorithm=self.LUHN_ALGORITHM,
                                                 exc_to_raise=exceptions.ValidationError)
        # when
        # then
        self.assertRaises(exceptions.ValidationError, validator.is_valid)
