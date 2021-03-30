from tabulate import tabulate
from utilities import get_val


def runge_kutta(f_expr, h, initial_state, to_find):
    table = [initial_state]
    curr = initial_state
    while curr[0] < to_find:
        k1 = h * get_val(f_expr, curr)
        k2 = h * get_val(f_expr, (curr[0] + h, curr[1] + k1))
        curr = (curr[0] + h, curr[-1] + (k1 + k2) / 2)
        table.append(curr)
    print(tabulate(table, headers=['X', 'PRED_Y'], tablefmt='psql'))
    return curr


def main():
    function_expr = 'x ** 2 + y'
    h = 0.01
    initial_state = (0, 1)
    to_find = 0.02
    print(f"f({to_find}) ~ {runge_kutta(function_expr, h, initial_state, to_find)[1]}")


if __name__ == '__main__':
    main()
