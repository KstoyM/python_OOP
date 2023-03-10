from functools import reduce
from typing import List


class Calculator:

    @staticmethod
    def add(*args: List[int]):
        return sum(args)

    @staticmethod
    def multiply(*args: List[int]):
        return reduce(lambda a, b: a * b, args)

    @staticmethod
    def divide(*args: List[int]):
        return reduce(lambda a, b: a / b, args)

    @staticmethod
    def subtract(*args: List[int]):
        return reduce(lambda a, b: a - b, args)


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
