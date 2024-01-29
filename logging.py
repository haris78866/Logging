import math
import logging

logging.basicConfig(level=logging.ERROR)

x = input('Enter the value for x: ')


def sqrt(x, guess=1.0):
    if float(x) < 0:
        logging.error("Cannot calculate the square root of a negative number.")
        return None
    else:
        return math.sqrt(float(x))


result = sqrt(x)

if result is not None:
    print('The result is', result)
