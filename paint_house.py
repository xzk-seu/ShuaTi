class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """

    def minCost(self, costs):
        # write your code here
        house_mun = len(costs)
        f = [[0, 0, 0], ]

        for i in range(1, house_mun + 1):
            row = list()
            for j in range(3):
                temp = [(f[i - 1][t] + costs[i - 1][j]) for t in range(3) if t != j]
                row.append(min(temp))
            f.append(row)
        res = min(f[-1])
        return res


if __name__ == '__main__':
    c = [[14, 2, 11], [11, 14, 5], [14, 3, 10]]
    s = Solution()
    r = s.minCost(c)
    print(r)
