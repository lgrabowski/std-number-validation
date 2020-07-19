import unittest

from std_number_validation import algorithms


class DammAlgorithmTestCase(unittest.TestCase):
    DAMM = algorithms.DammAlgorithm()
    CORRECT_NUMBER = 112946
    INCORRECT_NUMBER = 112950

    def setUp(self) -> None:
        pass

    def test_checks_if_damm_accepts_correct_number(self):
        """
        luhn should return true for valid number
        """
        # given
        # when
        is_valid = self.DAMM.is_valid(self.CORRECT_NUMBER)
        # then
        self.assertTrue(is_valid)

    def test_checks_if_damm_rejects_invalid_number(self):
        """
        luhn should return false for invalid number
        """
        # given
        # when
        is_valid = self.DAMM.is_valid(self.INCORRECT_NUMBER)
        # then
        self.assertFalse(is_valid)