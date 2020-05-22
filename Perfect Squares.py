class Solution_DP:
    """
    @param n: a positive integer
    @return: An integer
    """
    def numSquares(self, n):
        # write your code here
        # f[i]表示i最少有几个完全平方数组成
        while n % 4 == 0:
            n = n // 4
        if n % 8 == 7:
            return 4

        f = [float("inf") for _ in range(n+1)]

        i = 0
        while i * i < n:
            f[i * i] = 1
            i += 1

        for i in range(1, n+1):
            if f[i] == 1:
                continue
            j = 1
            while j * j <= i:
                temp = f[i-j * j] + 1
                f[i] = min(f[i], temp)
                j += 1
        return f[-1]


class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """

    def numSquares(self, n):
        # write your code here
        # f[i]表示i最少有几个完全平方数组成
        while n % 4 == 0:
            n = n // 4
        if n % 8 == 7:
            return 4

        sqrt_n = int(n ** 0.5)
        if sqrt_n ** 2 == n:
            return 1

        i = 0
        while i * i < n:
            i2 = i * i
            t = int((n - i2) ** 0.5)
            temp = t ** 2 + i2
            if temp == n:
                return 2
            i += 1
        return 3


if __name__ == '__main__':
    # c = 13
    c = 12
    # c = 1000000000
    s = Solution()
    r = s.numSquares(c)
    print(r)
