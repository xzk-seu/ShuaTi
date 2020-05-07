class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, k, prices):
        # write your code here
        n = len(prices)
        if n == 0:
            return 0

        if k > n // 2:
            res = 0
            for n, p in enumerate(prices[1:]):
                t = p - prices[n]
                if t > 0:
                    res += t
            return res

        f = [[0 for _ in range(2 * k + 1)] for _ in range(2)]
        res = 0

        temp_p = prices[0]
        for j, p in enumerate(prices[1:]):
            today_delta = p - temp_p
            temp_p = p

            t_1 = j % 2  # 上一天在状态里的坐标
            t = 1 - t_1  # 今天在状态里的坐标

            for a in range(k):
                own_num = 2 * a + 1
                emp_num = own_num + 1
                today_profit = f[t_1][own_num] + today_delta
                f[t][own_num] = max(today_profit, f[t_1][own_num - 1])
                f[t][emp_num] = max(f[t_1][emp_num], today_profit)
            if f[t][-1] > res:
                res = f[t][-1]
        return res


        # for i in range(1, n):
        #     t = i % 2
        #     t_1 = 1 - t
        #     today_delta = prices[i] - prices[i - 1]
        #     for j in range(k):
        #         own_num = 2 * j + 1
        #         emp_num = own_num + 1
        #         today_profit = f[t_1][own_num] + today_delta
        #         f[t][own_num] = max(today_profit, f[t_1][own_num - 1])
        #         f[t][emp_num] = max(f[t_1][emp_num], today_profit)
        #     if f[t][-1] > res:
        #         res = f[t][-1]
        # return res


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
    r = s.maxProfit(2, c)
    print(r)