import math
import time


def find_gcd(numbers: list):
    while len(numbers) > 1:
        tempGcd = math.gcd(numbers[0], numbers[1])
        numbers.pop(0)
        numbers[0] = tempGcd
        return find_gcd(numbers)
    return numbers[0]




def get_exception_printable_string(exception: Exception) -> str:
    return '[{} {}]'.format(type(exception).__name__, exception)
