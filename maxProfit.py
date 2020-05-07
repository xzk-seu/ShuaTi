class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        # 到今天为止的最低价
        lowest = float("inf")
        f = [0 for _ in prices]
        for n, p in enumerate(prices):
            if p < lowest:
                lowest = p
            f[n] = p-lowest
        return max(f)


if __name__ == '__main__':
    c = [3, 2, 3, 1, 2]
    s = Solution()
    r = s.maxProfit(c)
    print(r)
