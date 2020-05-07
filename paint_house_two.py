class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """

    def minCostII(self, costs):
        # write your code here
        house_mun = len(costs)
        if house_mun == 0:
            return 0
        color_num = len(costs[0])
        f = [[0 for _ in range(color_num)], ]

        for i in range(1, house_mun + 1):
            row = list()
            min1 = float("inf")
            min2 = float("inf")
            j1 = -1
            for t in range(color_num):
                temp = f[i - 1][t]
                if temp < min1:
                    min2 = min1
                    min1 = temp
                    j1 = t
                elif min2 > temp >= min1:
                    min2 = temp
            for t in range(color_num):
                if t == j1:
                    row.append(min2 + costs[i - 1][t])
                else:
                    row.append(min1 + costs[i - 1][t])
            f.append(row)
        res = min(f[-1])
        return res


if __name__ == '__main__':
    c = [[14, 2, 11], [11, 14, 5], [14, 3, 10]]
    s = Solution()
    r = s.minCostII(c)
    print(r)
