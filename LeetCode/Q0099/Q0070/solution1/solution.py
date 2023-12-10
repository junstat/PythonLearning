class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        while n > 0:
            a, b = b, a + b
            n -= 1
        return a


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(3))
