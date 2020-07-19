from std_number_validation import algorithms


class DammAlgorithm(algorithms.BaseAlgorithm):
    """
    Damm algorithm helps in detecting digits which are
    set incorrectly and errors as transposition in adjacency
    """

    MATRIX = (
        (0, 3, 1, 7, 5, 9, 8, 6, 4, 2),
        (7, 0, 9, 2, 1, 5, 4, 8, 6, 3),
        (4, 2, 0, 6, 8, 7, 1, 3, 5, 9),
        (1, 7, 5, 0, 9, 8, 3, 4, 2, 6),
        (6, 1, 2, 3, 0, 4, 5, 9, 7, 8),
        (3, 6, 7, 4, 2, 0, 9, 5, 8, 1),
        (5, 8, 6, 9, 7, 2, 0, 1, 3, 4),
        (8, 9, 4, 5, 3, 6, 2, 0, 1, 7),
        (9, 4, 3, 8, 6, 1, 7, 2, 0, 5),
        (2, 5, 8, 1, 4, 3, 6, 7, 9, 0)
    )


    def checksum(self, number: int) -> int:
        """
        returns value in matrix which is set by digit in entry number
        :param number:
        :return:
        """
        row = 0
        for digit in str(number):
            row = self.MATRIX[row][int(digit)]
        return row

    def is_valid(self, number: int) -> bool:
        """
        checksum has be 0
        :param number:
        :return:
        """
        return self.checksum(number) == 0