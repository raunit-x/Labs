from utilities import *
import sympy as sym
import re
from math_functions import MATH_FUNCTIONS


def newton(function_string, function_prime_string, x_0, max_error=1e-8):
    f_x0, f_x0_prime = get_function_val(function_string, x_0), get_function_val(function_prime_string, x_0)
    i = 0
    while abs(f_x0) > max_error:
        x_0 = x_0 - (f_x0 / f_x0_prime)
        f_x0, f_x0_prime = get_function_val(function_string, x_0), get_function_val(function_prime_string, x_0)
        print(f'{i}: {x_0:.5f}\t\t{f_x0:.5f}\t\t{f_x0_prime:.5f}')
        i += 1
    return x_0


def format_expr(expr):
    d = {val: f"np.{val}" for val in MATH_FUNCTIONS}
    str_in = expr
    return re.sub(r'\b(\w+)\b', lambda m: d.get(m.group(1), m.group(1)), str_in)


if __name__ == '__main__':
    function_expr = '2 * x - 6 - np.log10(x)'
    x = sym.Symbol('x')
    function_expr_prime = format_expr(str(sym.diff(function_expr.replace('np.', ''))))
    print(f'Function: {function_expr}\nFunction Prime: {function_expr_prime}')
    intervals = get_intervals(function_expr)
    for interval in intervals:
        print(f'Interval [{interval[0]}, {interval[1]}]: '
              f'{newton(function_expr, function_expr_prime, (interval[0] + interval[1]) / 2)}')
