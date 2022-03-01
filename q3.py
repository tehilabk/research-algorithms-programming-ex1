EPSILON = 0.0001

def find_root(func, a, b):
    xn = a
    steps = 1000
    for n in range(0, steps):
        f_xn = func(xn)
        if abs(f_xn) < EPSILON:
            return xn

        derivative_xn = (func(xn + EPSILON) - func(xn)) / EPSILON
        if derivative_xn == 0:
            raise Exception('No solution')

        # calculate next xn
        xn = xn - f_xn / derivative_xn

    return xn


