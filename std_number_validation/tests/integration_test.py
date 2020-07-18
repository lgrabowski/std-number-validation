import unittest

from std_number_validation import validate
from std_number_validation import exceptions


class IntegrationTestCase(unittest.TestCase):
    CORRECT_NUMBER = 79927398713
    INCORRECT_NUMBER = 79927398711

    def test_integration_should_accept_valid_number(self):
        # given
        # when
        is_valid = validate.validation(self.CORRECT_NUMBER).is_valid()
        # then
        self.assertTrue(is_valid)

    def test_integration_should_reject_invalid_number(self):
        # given
        # when
        is_valid = validate.validation(self.INCORRECT_NUMBER).is_valid()
        # then
        self.assertFalse(is_valid)

    def test_integration_should_reject_invalid_number_and_raise_exception(self):
        # given
        validator = validate.validation(self.INCORRECT_NUMBER, exc_to_raise=exceptions.ValidationError)
        # when
        # then
        self.assertRaises(exceptions.ValidationError, validator.is_valid)

    def test_integration_should_reject_invalid_number_via_contextual_validation(self):
        # given
        with validate.contextual_validation(self.INCORRECT_NUMBER,
                                            exc_to_raise=exceptions.ValidationError) as validator:
            # when
            # then
            self.assertRaises(exceptions.ValidationError, validator.is_valid)
