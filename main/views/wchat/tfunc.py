import time


def to_localtime(timestamp):
    time_Array = time.localtime(int(timestamp))
    other_StyleTime = time.strftime("%Y-%m-%d %H:%M:%S", time_Array)
    return other_StyleTime
