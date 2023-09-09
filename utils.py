class utils:
    @staticmethod
    def reversed(n: int) -> int:
        stringInput = str(n)
        stringOutput = ''
        for c in stringInput:
            stringOutput = c + stringOutput
        return int(stringOutput)

    @staticmethod
    def formatter(n: int) -> list[str]:
        retArray = [bin(n), oct(n)]
        return retArray
