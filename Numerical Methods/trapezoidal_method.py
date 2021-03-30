import numpy as np
from utilities import *


def trapezoidal_integration(f_x, a, b, n):
    del_x = (b - a) / n
    f_a, f_b = get_function_val(f_x, a), get_function_val(f_x, b)
    return del_x / 2 * (sum([2 * get_function_val(f_x, a + i * del_x) for i in range(n + 1)]) - f_b - f_a)


if __name__ == '__main__':
    function_expr = 'x ** 2'
    lower_limit = 0
    upper_limit = 10
    n = 5
    print(f"Approx integral of '{function_expr}' from {lower_limit} to "
          f"{upper_limit}: {trapezoidal_integration(function_expr, lower_limit, upper_limit, n)}")
