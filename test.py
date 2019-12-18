from functools import reduce


def f(s):
    print(s)


r = list('impython')


def add(a, b):
    return a + b


R = reduce(add, r)


