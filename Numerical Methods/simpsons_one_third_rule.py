import numpy as np
from utilities import *


def simpsons_integration_rule(f_x, a, b):
    h = (b - a) / 2
    f_a = get_function_val(f_x, a)
    f_b = get_function_val(f_x, b)
    f_a_b_2 = get_function_val(f_x, (a + b) / 2)
    return h / 3 * (f_a + f_b + 4 * f_a_b_2)


if __name__ == '__main__':
    function_expr = '5 * x * np.exp(-2 * x)'
    lower_limit = .1
    upper_limit = 1.3
    print(f"Approx integral of '{function_expr}' from {lower_limit} to "
          f"{upper_limit}: {simpsons_integration_rule(function_expr, lower_limit, upper_limit)}")
