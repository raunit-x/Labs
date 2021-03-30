from tabulate import tabulate
import numpy as np

facts = {}  # cache for factorials


# calculating u mentioned in the formula
def u_cal(u_loc, num):
    temp = 1
    for i in range(num):
        temp *= (u_loc + i)
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
    x = [1891, 1901, 1911, 1921, 1931]

    # difference table
    y = np.zeros((n, n))
    y[:, 0] = [46, 66, 81, 93, 101]

    # Calculating the forward difference
    # table
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = y[j + 1][i - 1] - y[j][i - 1]
    print_table(x, y)
    # Value to interpolate at
    value = 1925
    # initializing u and sum
    sum = y[-1][0]
    u = (x[-1] - value) / (x[-2] - x[-1])
    for i in range(1, n):
        sum += (u_cal(u, i) * y[-i - 1][i]) / fact(i)
    print(f"\nValue at {value} is: {round(sum, 6)}")
