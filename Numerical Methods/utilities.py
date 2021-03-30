import numpy as np


# assume the variable to be 'x'
def get_function_val(function_string, i):
    x = i
    return eval(function_string)


# assume the variable to be 'x'
def get_intervals(function_string, low=-50, high=50):
    y = []
    X = [val for val in range(low, high + 1)]
    for val in X:
        x = val
        y.append(eval(function_string))
    flag = [y[0] > 0, X[0]]
    intervals_loc = []
    for i, val in enumerate(y):
        condition = (val > 0) != flag[0]
        if condition:
            intervals_loc.append([flag[1], X[i]])
        flag = [not flag[0] if condition else flag[0], X[i]]
    return intervals_loc


def get_val(f_prime, state):
    x, y = state
    return eval(f_prime)
