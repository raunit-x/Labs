import numpy as np
import string

VARS = string.ascii_letters


def generate_variables(num):
    for i in range(num):
        globals()[f'{VARS[i]}'] = 0


def get_value(expr, vals):
    def set_vars():
        for i, val in enumerate(vals):
            globals()[f'{VARS[i]}'] = val
    set_vars()
    return eval(expr)


def parse(equations):
    coeffs = []
    z = []
    for equation in equations:
        l, r = equation.split('=')
        equation = l
        z.append(float(r.strip()))
        terms = [val.strip() for val in equation.split('+') if val and val.strip()[-1] in VARS]
        coeff = [float('1' if len(term) == 1 else term[:-1]) for term in terms]
        coeffs.append(coeff)
    return np.array(coeffs), np.array(z)


def form_equations(coeffs, z):
    symbolic_equations = []
    for z_it, coeff in zip(z, coeffs):
        idx = np.argmax(coeff)
        sym_eq = " + ".join([f'{-coeff[i]} * {VARS[i]}' for i in range(len(coeff)) if i != idx] + [f"{z_it}"])
        symbolic_equations.append(f"({sym_eq}) / {coeff[idx]}")
    return symbolic_equations


def gauss_jacobi(sym_equations, num_iterations=10):
    vals = [0 for _ in range(len(sym_equations))]
    for _ in range(num_iterations):
        temp = [val for val in vals]
        for i, sym_eq in enumerate(sym_equations):
            temp[i] = get_value(sym_eq, vals)
        vals = temp
    print(f"APPROX VALUES: {vals}")


def main():
    equations = ['27x + 6y + -1z = 85',
                 '6x + 15y + 2z = 72',
                 'x + y + 54z = 110']
    coeffs, z = parse(equations)
    print(f"COEFFS: \n{coeffs}")
    print(f"B: \n{z}\n")
    sym_equations = form_equations(coeffs, z)
    print(f"SYSTEM OF EQUATIONS: {sym_equations}")
    gauss_jacobi(sym_equations, 5)


if __name__ == '__main__':
    main()
