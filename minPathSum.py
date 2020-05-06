class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """

    def minPathSum(self, grid):
        # write your code here
        raw = len(grid)
        col = len(grid[0])
        f = [[0 for _ in range(col)] for _ in range(2)]
        i1 = 0
        for i in range(raw):
            for j in range(col):
                i1 = i % 2
                up = f[i1 - 1][j] + grid[i][j]
                le = f[i1][j - 1] + grid[i][j]
                if i == 0 and j == 0:
                    f[i1][j] = grid[i][j]
                    continue
                elif i == 0:
                    f[i1][j] = le
                elif j == 0:
                    f[i1][j] = up
                else:
                    f[i1][j] = min(le, up)
        return f[i1][-1]


if __name__ == '__main__':
    c = [[7, 4, 8, 7, 9, 3, 7, 5, 0],
         [1, 8, 2, 2, 7, 1, 4, 5, 7],
         [4, 6, 4, 7, 7, 4, 8, 2, 1],
         [1, 9, 6, 9, 8, 2, 9, 7, 2],
         [5, 5, 7, 5, 8, 7, 9, 1, 4],
         [0, 7, 9, 9, 1, 5, 3, 9, 4]]
    # c = [[1,3,1],[1,5,1],[4,2,1]]
    s = Solution()
    r = s.minPathSum(c)
    print(r)
