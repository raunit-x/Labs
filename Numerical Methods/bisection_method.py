import numpy as np
from utilities import *


def bisect(function_string, a, b, counter=0, max_error=1e-10):
    if abs(get_function_val(function_string, (a + b) / 2)) < max_error:
        return (a + b) / 2
    f_a, f_b = get_function_val(function_string, a), get_function_val(function_string, b)
    mid = get_function_val(function_string, (a + b) / 2)
    print(f'{counter}: {a:.5f}\t\t{b:.5f}\t\t{((a + b) / 2):.5f}\t\t{get_function_val(function_string, (a + b) / 2):.5f}')
    if not mid:
        return (a + b) / 2
    if f_a * mid < 0:
        return bisect(function_string, a, (a + b) / 2, counter + 1)
    else:
        return bisect(function_string, (a + b) / 2, b, counter + 1)


if __name__ == '__main__':
    function_expr = 'x ** 3 - 4 * x + 9'
    intervals = get_intervals(function_expr)
    for interval in intervals:
        print(f'Interval [{interval[0]}, {interval[1]}]: {bisect(function_expr, interval[0], interval[1])}')
