class utils:
    @staticmethod
    def reversed(n: int) -> int:
        if not isinstance(n, int):
            raise TypeError

        negative = False
        if n < 0:
            negative = True
            n = -n
        stringInput = str(n)
        stringOutput = ''
        for c in stringInput:
            stringOutput = c + stringOutput
        returnInt = int(stringOutput)
        if negative:
            returnInt = -returnInt
        return returnInt

    @staticmethod
    def formatter(n: int) -> list[str]:
        if not isinstance(n, int):
            raise TypeError
        retArray = [bin(n), oct(n)]
        return retArray
