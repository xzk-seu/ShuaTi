class Solution_DP:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        # f[i][w]表示到前i个物品，拼出体积w的最大价值，拼不出为-1

        n = len(A)
        f = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
        f[0][0] = 0

        for i in range(n):
            for w in range(m + 1):
                t1 = -1
                t2 = -1
                if w >= A[i]:
                    t1 = f[i][w - A[i]]
                if t1 >= 0:
                    t2 = t1 + V[i]
                t3 = f[i][w]
                f[i + 1][w] = max(t2, t3)

        return max(f[-1])


class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        # f[i][w]表示到前i个物品，拼出体积w的最大价值，拼不出为-1

        n = len(A)
        f = [-1 for _ in range(m + 1)]
        f[0] = 0

        for i in range(n):
            for w in reversed(range(m + 1)):
                t2 = -1
                i2 = w - A[i]
                if i2 >= 0 and f[i2] >= 0:
                    t2 = f[i2] + V[i]
                f[w] = max(t2, f[w])

        return max(f)


if __name__ == '__main__':
    """
    Input: m = 10, A = [2, 3, 5, 7], V = [1, 5, 2, 4]
    Output: 9
    """
    p1 = 10
    p2 = [2, 3, 5, 7]
    p3 = [1, 5, 2, 4]
    st = Solution()
    r = st.backPackII(p1, p2, p3)
    print(r)
