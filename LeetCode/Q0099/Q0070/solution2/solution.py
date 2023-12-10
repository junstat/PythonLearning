class Solution:
    def climbStairs(self, n: int) -> int:
        return self.fib(n, 1, 1)

    def fib(self, n, a, b):
        return a if n == 0 else self.fib(n - 1, b, a + b)
