def ro(x, a, b):
    return a * x * (b - x)


def _id(arg):
    return arg


class Solver:
    def __init__(self):
        self.ro = _id
        self.s = _id
        self.z = _id

    def set_parameters(self, *args, **kwargs):
        pass

    def write_tabular(self):
        pass

    def create_ro(self, a, b):
        def _r(x):
            return ro(x, a, b)

        self.ro = _r

    def create_s(self, expr):
        def f(t):
            return eval(expr)

        self.s = f

    def create_z(self, expr):
        def f(t):
            return eval(expr)

        self.z = f

