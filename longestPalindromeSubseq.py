class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longestPalindromeSubseq(self, s):
        # write your code here
        n = len(s)
        if n == 0:
            return 0
        f = [[0 for _ in s] for _ in s]
        for i in range(n):
            f[i][i] = 1

        for i in range(n - 1):
            j = i + 1
            if s[i] == s[j]:
                f[i][j] = 2
            else:
                f[i][j] = 1

        for t in range(2, n):
            for i in range(n-t):
                j = i + t
                f[i][j] = max(f[i + 1][j], f[i][j - 1])
                if s[i] == s[j]:
                    f[i][j] = max(f[i][j], f[i+1][j-1] + 2)
        return f[0][-1]


if __name__ == '__main__':
    c = "bbbab"
    st = Solution()
    r = st.longestPalindromeSubseq(c)
    print(r)