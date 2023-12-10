import weakref


class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args, **kwargs):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args, **kwargs)
            self.__cache[args] = obj
            return obj


# Example
class Spam(metaclass=Cached):
    def __init__(self, name):
        print(f'CreatingSpam({name!r})')
        self.name = name


if __name__ == '__main__':
    a = Spam('Guido')
    b = Spam('Diana')
    c = Spam('Guido')
    print(a is b, a is c)
