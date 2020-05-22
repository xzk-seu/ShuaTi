class Solution:
    """
    @param s: A string
    @return: An integer
    """

    def minCut(self, s):
        # write your code here
        # 前i个字符组成的子串的最少划分次数
        n = len(s)
        f = [i for i in range(n + 1)]
        is_p = [[False for _ in s] for _ in s]
        f[0] = 0
        for i in range(n):
            for j in reversed(range(i + 1)):
                if s[i] == s[j] and (i - j < 2 or is_p[j + 1][i - 1]):
                    is_p[j][i] = True
                    f[i + 1] = min(f[i + 1], f[j] + 1)
        return f[-1] - 1


if __name__ == '__main__':
    c = "aab"
    st = Solution()
    r = st.minCut(c)
    print(r)
