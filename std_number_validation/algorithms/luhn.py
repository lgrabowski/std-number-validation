from std_number_validation import algorithms


class LuhnAlgorithm(algorithms.BaseAlgorithm):
    """
    Luhn algorithm
    over the given alphabet we can decide if
    given number is valid in terms miss spelling it.

    In digits of number have been moved by accident we can detect it.
    """

    BASE_ALPHABET = "0123456789"

    def checksum(self, number: int) -> int:
        """
        Luhn algorithm, sum of odd number with sum of digits of double even number
        module len of alphabet
        Thanks to python rich list slicing interface we can
        list[Position::Step] from right side with step

        :param number:
        :return:
        """
        return sum(self.to_digits(number)[-1::-2]) + \
               sum([sum(self.to_digits(d*2)) for d in self.to_digits(number)[-2::-2]])

    def to_digits(self, number):
        return list(map(int, str(number)))

    def is_valid(self, number: int) -> bool:
        """
        execute check against Luhn validators condition
        :param number:
        :return: bool
        """
        return self.checksum(number) % len(self.BASE_ALPHABET) == 0




