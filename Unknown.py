from ValueTree import *


class Unknown(TNumber):
    name = ""
    name_num = ord('a')

    def __init__(self, value):
        super().__init__(value)
        if isinstance(value, str):
            self.value_tree = ValueTree(value)
            self.value = self.value_tree.out()
            self.size = self.value_tree.get_size()

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

    def out(self):
        if self.size == 1:
            self.name = self.value
        else:
            self.name = chr(self.name_num)

    def print_hello(self):
        self.out()
        print("Hello " + self.name)
