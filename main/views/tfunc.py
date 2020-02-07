import functools
import string
import time


# 时间戳转换为本地时间


def to_localtime(timestamp):
    time_Array = time.localtime(int(timestamp))
    other_StyleTime = time.strftime("%Y-%m-%d %H:%M:%S", time_Array)
    return other_StyleTime


# 装饰器模板
def func(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)

    return wrapper


# FIFO
class Queue(object):
    def __init__(self):
        self.list = []

    def _in(self, parameter):
        self.list.append(parameter)
        return self.list

    def _out(self):
        header = self.list[0]
        self.list = self.list[1:]
        return header

    def show(self):
        return self.list


def U(s):
    return string.capwords(s)


# 反解码url
def unquote(url):
    from urllib.parse import unquote, unquote_plus
    return unquote(url)
