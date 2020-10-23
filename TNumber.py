from enum import Enum, unique


def compare(char):
    if isinstance(char, str):
        if len(char) > 1:
            return False
        for i in Mark:
            if i.value == char:
                return True

    return False


def lever(num) -> str:
    if num == 1:
        return Mark.Add.value + Mark.Sub.value
    elif num == 2:
        return Mark.Mul.value + Mark.Div.value
    elif num == 3:
        return Mark.Pow.value
    else:
        return Mark.Brl.value + Mark.Brr.value


@unique
class Mark(Enum):
    Add = '+'
    Sub = '-'
    Mul = '*'
    Div = '/'
    Pow = '^'
    Brl = '('
    Brr = ')'


class TNumber(object):
    def __init__(self, value):
        self.value = value

    def add(self, b):
        pass

    def minus(self, b):
        pass

    def times(self, b):
        pass

    def scalar(self, k):
        pass

    def divides(self, b):
        pass

    def pow(self, k):
        pass
