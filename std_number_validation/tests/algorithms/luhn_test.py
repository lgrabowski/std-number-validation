import unittest

from std_number_validation import algorithms

class LuhnAlgorithmTestCase(unittest.TestCase):

    LUHN = algorithms.LuhnAlgorithm()
    CORRECT_NUMBER = 4532015112830366
    INCORRECT_NUMBER = 4532015112830311
    INCORRECT_NUMBER_SWAPPED_DIGITS = 4532015112830636

    def setUp(self) -> None:
        pass

    def test_checks_if_luhn_accepts_correct_number(self):
        """
        luhn should return true for valid number
        """
        # given
        # when
        is_valid = self.LUHN.is_valid(self.CORRECT_NUMBER)
        # then
        self.assertTrue(is_valid)

    def test_checks_if_luhn_rejects_invalid_number(self):
        """
        luhn should return false for invalid number
        """
        # given
        # when
        is_valid = self.LUHN.is_valid(self.INCORRECT_NUMBER)
        # then
        self.assertFalse(is_valid)

    def test_checks_if_luhn_rejects_invalided_number_with_by_swapped_digits(self):
        """
        luhn should return false for invalided number by swapping digits
        """
        # given
        # when
        is_valid = self.LUHN.is_valid(self.INCORRECT_NUMBER_SWAPPED_DIGITS)
        # then
        self.assertFalse(is_valid)

    def test_checks_if_luhn_rejects_invalid_numbers(self):
        """
        luhn should return false for invalided number by swapping digits
        """
        # given
        invalid_numbers = [0, -1, 0.04, b'010010', ]
        # when
        for number in invalid_numbers:
            # then
            self.assertFalse(self.LUHN.is_valid(self.INCORRECT_NUMBER_SWAPPED_DIGITS),
                             msg=f"{number} was incorrectly accepted")
