from functools import wraps

"""
9.3 解除一个装饰器
问题: 一个装饰器已经作用在一个函数上，你想撤销它，直接访问原始的未包装的那个函数
"""


def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator 1")
        return func(*args, **kwargs)

    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator 2")
        return func(*args, **kwargs)

    return wrapper


@decorator1
@decorator2
def add(x, y):
    return x + y


print(add(1, 2))
print("-" * 30)
print(add.__wrapped__(1, 2))
print("-" * 30)
print(add.__wrapped__.__wrapped__(1, 2))
