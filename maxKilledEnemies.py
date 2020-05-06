class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    def maxKilledEnemies(self, grid):
        # write your code here
        raw = len(grid)
        if raw == 0:
            return 0
        col = len(grid[0])
        up = [[0 for _ in range(col)] for _ in range(raw)]
        left = [[0 for _ in range(col)] for _ in range(raw)]
        down = [[0 for _ in range(col)] for _ in range(raw)]
        right = [[0 for _ in range(col)] for _ in range(raw)]
        res = [[0 for _ in range(col)] for _ in range(raw)]

        for i1 in range(raw):
            for j1 in range(col):
                i2 = raw - 1 - i1
                j2 = col - 1 - j1

                if grid[i1][j1] == "E":
                    up[i1][j1] += 1
                    left[i1][j1] += 1
                if i1 > 0:
                    up[i1][j1] += up[i1 - 1][j1]
                if j1 > 0:
                    left[i1][j1] += left[i1][j1 - 1]
                if grid[i1][j1] == "W":
                    up[i1][j1] = 0
                    left[i1][j1] = 0
                res[i1][j1] += up[i1][j1]
                res[i1][j1] += left[i1][j1]

                if grid[i2][j2] == "E":
                    down[i2][j2] += 1
                    right[i2][j2] += 1
                if i2 < raw - 1:
                    down[i2][j2] += down[i2 + 1][j2]
                if j2 < col - 1:
                    right[i2][j2] += right[i2][j2 + 1]
                if grid[i2][j2] == "W":
                    down[i2][j2] = 0
                    right[i2][j2] = 0
                res[i2][j2] += down[i2][j2]
                res[i2][j2] += right[i2][j2]

        m = 0
        for i in range(raw):
            for j in range(col):
                if grid[i][j] == "E":
                    continue
                if res[i][j] > m:
                    m = res[i][j]

        return m


if __name__ == '__main__':
    c = ["0E00",
         "E0WE",
         "0E00"]
    s = Solution()
    r = s.maxKilledEnemies(c)
    print(r)
