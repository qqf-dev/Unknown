import TNumber

from enum import Enum


class Mark(Enum):
    Add = '+'
    Sub = '-'
    Mul = '*'
    Div = '/'
    Pow = '^'


class Unknown(TNumber.TNumber):
    def __init__(self, value):
        self.value = value
        self.valueSpace = None
        self.numberSpace = None
        self.powerSpace = None

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

    def power(self, k):
        pass

    def printHello(self):
        print("Hello " + self.value)
