class BaseAlgorithm:

    def checksum(self, number: int) -> int:
        raise NotImplementedError("This method must be implemented")

    def is_valid(self, number: int) -> bool:
        raise NotImplementedError("This method must be implemented")
