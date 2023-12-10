class NoInstance(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")


# Example
class Spam(metaclass=NoInstance):
    @staticmethod
    def grok(x):
        print("Spam.grok")


Spam.grok(42)
# s = Spam()
