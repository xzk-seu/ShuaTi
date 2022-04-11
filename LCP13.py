class Solution:
    @staticmethod
    def minimalSteps(maze) -> int:
        if len(maze) == 0 or len(maze[0]) == 0:
            return -1
        m = len(maze)
        n = len(maze[0])

        def neighbours(x, y):  # 定义相邻点
            nearby = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            return [each for each in nearby if 0 <= each[0] < m and 0 <= each[1] < n]

        s = None
        t = None
        m_list = list()
        o_list = list()
        for i in range(m):
            for j in range(n):
                if maze[i][j] == "S":
                    s = [i, j]
                elif maze[i][j] == "T":
                    t = [i, j]
                elif maze[i][j] == "M":
                    m_list.append([i, j])
                elif maze[i][j] == "O":
                    o_list.append([i, j])

        nb = len(m_list)

        def get_distance(begin, end):
            distance = [[-1 for _ in range(n)] for _ in range(m)]
            if begin[0] == end[0] and begin[1] == end[1]:
                return 0

            # BFS
            queue = [begin]
            distance[begin[0]][begin[1]] = 0
            while len(queue) != 0:
                temp_i, temp_j = queue.pop(0)
                for neighbour in neighbours(temp_i, temp_j):
                    new_i = neighbour[0]
                    new_j = neighbour[1]
                    if maze[new_i][new_j] != "#" and distance[new_i][new_j] == -1:
                        queue.append([new_i, new_j])
                        distance[new_i][new_j] = distance[temp_i][temp_j] + 1
            res = distance[end[0]][end[1]]
            return res

        if nb == 0:
            return get_distance(s, t)
        # 记录第i个石头到第j个机关的最短距离
        # dist_stone[i][-2]表示到起点的距离， dist_stone[i][-1]表示到终点的距离
        dist_stone = [[-1 for _ in range(len(m_list)+2)] for _ in range(len(o_list))]
        for i in range(len(o_list)):
            for j in range(len(m_list)):
                dist_stone[i][j] = get_distance(o_list[i], m_list[j])
            dist_stone[i][-2] = get_distance(o_list[i], s)
            dist_stone[i][-1] = get_distance(o_list[i], t)

        # 记录第i个机关到第j个机关的最短距离，跨越石头
        # dist[i][nb]表示到起点的距离， dist[i][nb+1]表示到终点的距离
        dist = [[-1] * (len(m_list) + 2) for _ in range(len(m_list))]
        for i in range(len(m_list)):
            for j in range(i + 1, len(m_list)+2):
                dis_i_j = float("inf")
                for k in range(len(o_list)):
                    if dist_stone[k][i] > 0 and dist_stone[k][j] > 0:
                        temp_dis = dist_stone[k][i] + dist_stone[k][j]
                        dis_i_j = min(temp_dis, dis_i_j)
                dist[i][j] = dis_i_j if dis_i_j != float("inf") else -1
                if j < len(m_list):
                    dist[j][i] = dis_i_j
                dist[i][-1] = get_distance(m_list[i], t)

        # 若有任意一个机关 到起点或终点没有路径(即为-1),则说明无法达成，返回-1
        for i in range(nb):
            if dist[i][nb] == -1 or dist[i][nb + 1] == -1:
                return -1
        # dp数组， -1代表没有遍历到, 1<<nb表示题解中提到的mask, dp[mask][j]表示当前处于第j个机关，总的触发状态为mask所需要的最短路径, 由于有2**nb个状态，因此1<<nb的开销必不可少
        dp = [[-1] * len(m_list) for _ in range(1 << len(m_list))]

        # 初识状态，即从start到第i个机关，此时mask的第i位为1，其余位为0
        for i in range(nb):
            dp[1 << i][i] = dist[i][nb]

        for mask in range(1, (1 << nb)):
            for i in range(nb):
                # 若当前位置是正确的，即mask的第i位是1
                if mask & (1 << i) != 0:
                    for j in range(nb):
                        # 选择下一个机关j,要使得机关j目前没有到达，即mask的第j位是0
                        if mask & (1 << j) == 0:
                            next_mask = mask | (1 << j)
                            if dp[next_mask][j] == -1 or dp[next_mask][j] > dp[mask][i] + dist[i][j]:
                                dp[next_mask][j] = dp[mask][i] + dist[i][j]

        # 最后一个机关到终点
        ans = -1
        final_mask = (1 << nb) - 1
        for i in range(nb):
            if ans == -1 or ans > dp[final_mask][i] + dist[i][nb + 1]:
                ans = dp[final_mask][i] + dist[i][nb + 1]
        return ans


def main():
    s = Solution()
    s.minimalSteps(maze=["S#O", "M.#", "M.T"])
    # ["OOOOO","OS#OO","#O#TO","M#OOO"] -1
    # ["S#O", "M..", "M.T"] 16
    #  ["S#O", "M.T", "M.."] 17
    # ["S#O", "M.#", "M.T"] -1
    # ["S#O", "M.#", "M.T"] -1
    # ["S.#.M","O.#.O","M.#.T"] -1
    # ["##TOO#O#", "OO##O.S#", "###.O###", "#..O#O##"] 5
    # [".MM..", "#..M.", ".#..#", "..O..", ".S.OM", ".#M#T", "###..", "....."] 28
    # ["T#O", ".##", "O..", ".#.", "OSM", "#.."] 9


if __name__ == '__main__':
    main()
