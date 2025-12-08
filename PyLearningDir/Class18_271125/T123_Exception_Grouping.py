
exc_grp = ExceptionGroup("Multiple Ex", [
    ValueError("Invalid Value"),
    TypeError("Type Error "),
    ZeroDivisionError("Can't div Xero")
])


def check_div(a):
    if a == 0:
        raise exc_grp
    else:
        print(a)
check_div(2)