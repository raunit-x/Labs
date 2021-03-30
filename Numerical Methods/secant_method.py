from utilities import *
import numpy as np


def secant(function_string, x_0, x_1, max_error=1e-10):
    f_x0, f_x1 = get_function_val(function_string, x_0), get_function_val(function_string, x_1)
    x_2 = (x_0 * f_x1 - x_1 * f_x0) / (f_x1 - f_x0)
    f_x2 = get_function_val(function_string, x_2)
    i = 0
    while abs(f_x2) < max_error or (f_x1 != f_x0):
        x_0 = x_1
        x_1 = x_2
        f_x0 = f_x1
        f_x1 = f_x2
        if f_x1 == f_x0:
            break
        x_2 = (x_0 * f_x1 - x_1 * f_x0) / (f_x1 - f_x0)
        f_x2 = get_function_val(function_string, x_2)
        print(f'{i}: {x_0:.5f}\t\t{x_1:.5f}\t\t{x_2:.5f}\t\t{f_x2:.5f}')
    return x_2


if __name__ == '__main__':
    function_expr = 'x ** 3 - 4 * x + 9'
    intervals = get_intervals(function_expr)
    for interval in intervals:
        print(f'Interval [{interval[0]}, {interval[1]}]: {secant(function_expr, interval[0], interval[1])}')
