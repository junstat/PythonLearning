import time
from functools import wraps

"""
9.1 在函数上添加包装器
问题: 想在函数上添加一个包装器，增加额外的操作处理(比如日志、计时等)
"""


def time_this(func):
    """
    Decorator the reports the execution time.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@time_this
def countdown(n):
    while n > 0:
        n -= 1


countdown(100000)
