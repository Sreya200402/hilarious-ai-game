#console based calci using modules and "import"


def sqrt(x):
    if x < 0:
        return "Error : Negative Value"
    return x ** 0.5


def expo(a, b):
    return a ** b



def root(a, b):
    if b == 0:
         return "Error: Root by zero"
    return a ** (1 / b)
