from utilities import *
import numpy as np


def false_position(function_string, a, b, counter=0, max_error=1e-10):
    if abs(get_function_val(function_string, a)) < max_error:
        return a
    f_a, f_b = get_function_val(function_string, a), get_function_val(function_string, b)
    c = (a * f_b - b * f_a) / (f_b - f_a)
    f_c = get_function_val(function_string, c)
    print(f'{counter}: {a:.5f}\t\t{b:.5f}\t\t{c:.5f}\t\t{f_c:.5f}')
    if f_a * f_c < 0:
        return false_position(function_string, a, c, counter + 1)
    else:
        return false_position(function_string, c, b, counter + 1)


if __name__ == '__main__':
    function_expr = 'x ** 3 - 4 * x + 9'
    intervals = get_intervals(function_expr)
    for interval in intervals:
        print(f'Interval [{interval[0]}, {interval[1]}]: {false_position(function_expr, interval[0], interval[1])}')
