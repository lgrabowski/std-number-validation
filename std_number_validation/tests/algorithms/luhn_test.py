import unittest

from std_number_validation import algorithms

class LuhnAlgorithmTestCase(unittest.TestCase):

    LUHN = algorithms.LuhnAlgorithm()


    def setUp(self) -> None:
        pass


    def test_checks_if_luhn_calculates_correct_checksum(self):
        """
        luhn should return correct checksum
        """
        # given
        # when
        checksum = self.LUHN.checksum(10)