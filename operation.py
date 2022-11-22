memory = 0

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a // b

OPERATIONS = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}

def calculate(a, b, op):
    """
    Ф-ция выполняющ
    :param a:
    :param b:
    :param op:
    :return:
    """
    return OPERATIONS[op](a, b) 