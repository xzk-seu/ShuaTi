class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        res = 0
        for n, p in enumerate(prices[1:]):
            t = p - prices[n]
            if t > 0:
                res += t
        return res


if __name__ == '__main__':
    # 贪心
    c = [2, 1, 2, 0, 1]
    s = Solution()
    r = s.maxProfit(c)
    print(r)
