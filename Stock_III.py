class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        n = len(prices)
        if n == 0:
            return 0
        f = [[0 for _ in range(4)] for _ in prices]
        res = 0

        temp_p = prices[0]
        for j, p in enumerate(prices[1:]):
            today_delta = p - temp_p
            temp_p = p
            i = j + 1
            today_profit1 = f[j][0] + today_delta
            today_profit2 = f[j][2] + today_delta
            f[i][0] = max(0, today_profit1)
            f[i][1] = max(f[j][1], today_profit1)
            f[i][2] = max(today_profit2, f[j][1])
            f[i][3] = max(f[j][3], today_profit2)
            if f[i][3] > res:
                res = f[i][3]
        return res


if __name__ == '__main__':
    # state 0: 没买  1:第一次持有 2:第一次清仓 3:第二次持有 4:第二次清仓
    # f[i][j]: 在第i天结束后处于状态j的最大收益
    # f[i][0]: 第i天一直没买，所以一直为0
    # f[i][1]: 第i天持有，可能是i天买的， 收益为0；prices[i] - prices[i - 1]，可能是i-1天就持有的，f[i - 1][1] + today_delta
    # f[i][2]: 第i天清仓，可能是i-1天前就已经清仓，f[i - 1][2]，
    #          可能是i-1天才清仓，f[i - 2][1]+
    # f[i][3]: 第i天持有，可能是i-1天买的，prices[i] - prices[i - 1]，可能是i-1天就持有的，f[i - 1][1]
    # f[i][2]: 第i天清仓，可能是i-1天就已经清仓，可能是i-1天就已经清仓，f[i - 1][2]
    c = [4,4,6,1,1,4,2,5]
    s = Solution()
    r = s.maxProfit(c)
    print(r)