from tabulate import tabulate
import numpy as np
import math

facts = {}  # cache for factorials


# calculating u mentioned in the formula
def u_cal(u_loc, num):
    temp = 1
    for i in range(num):
        temp = temp * (u_loc - i)
    return temp


# calculating factorial of given number n
def fact(val):
    if val <= 1:
        return 1
    if i in facts:
        return facts[i]
    facts[i] = val * fact(val - 1)
    return facts[i]


# Displaying the forward difference table
def print_table(interval_x, output_y):
    table = np.zeros((n, n + 1))
    table[:, 0] = interval_x
    table[:, 1:] = output_y
    headers = ['X', 'Y']
    indentation = '  ' + '\t' * (n + 1)
    print(f"\n {indentation}Difference Table".upper())
    for i in range(1, n):
        headers.append(f"del_{i}_y")
    print(tabulate(table, headers=headers, tablefmt='psql'))


if __name__ == '__main__':

    n = 5
    x = [45, 50, 55, 60, 65]

    # difference table
    y = np.zeros((n, n))
    y[:, 0] = [0.7071, 0.7660, 0.8192, 0.8660, np.sin(math.radians(x[-1]))]

    # Calculating the forward difference
    # table
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

    print_table(x, y)

    # Value to interpolate at
    value = 52

    # initializing u and sum
    sum = y[0][0]
    u = (value - x[0]) / (x[1] - x[0])
    for i in range(1, n):
        sum += (u_cal(u, i) * y[0][i]) / fact(i)

    print(f"\nValue at {value} is: {round(sum, 6)}")
