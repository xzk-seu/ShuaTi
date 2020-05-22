class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        # f[i][w]表示到前i个物品，能否拼出w
        n = len(A)
        f = [[True for _ in range(m+1)] for _ in range(n+1)]
        for t in f:
            t[0] = True
        for i, a in enumerate(A):
            for j in range(m+1):
                if f[i][j] or (a <= j and f[i][j - a]):
                    f[i+1][j] = True

        for i, j in enumerate(reversed(f[-1])):
            if j:
                return m-i


if __name__ == '__main__':
    p1 = [3,4,8,5]
    p2 = 10
    st = Solution()
    r = st.backPack(p2, p1)
    print(r)