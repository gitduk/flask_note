import os
import time


def f(func):
    def wraper(*x):
        func(*x)
    return wraper


@f
def F(x):
    print('the num is %d' % x)



F(1000000)