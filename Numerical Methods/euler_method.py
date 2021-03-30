from tabulate import tabulate
from utilities import get_val


def euler(f_expr, h, initial_state, to_find):
    table = [initial_state]
    curr = initial_state
    while curr[0] < to_find:
        f_prime_x_y = get_val(f_expr, curr)
        curr = (curr[0] + h, curr[-1] + h * f_prime_x_y)
        table.append(curr)
    print(tabulate(table, headers=['X', 'PRED_Y'], tablefmt='psql'))
    return curr


def main():
    function_expr = 'x + 2 * y'
    h = 0.1
    initial_state = (2, 3)
    to_find = 2.5
    print(f"f({to_find}) ~ {euler(function_expr, h, initial_state, to_find)[1]}")


if __name__ == '__main__':
    main()
