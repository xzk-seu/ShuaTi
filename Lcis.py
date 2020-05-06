class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence(self, A):
        if len(A) == 0:
            return 0
        # write your code here
        f = [1 for _ in A]
        g = [1 for _ in A]
        for i in range(1, len(A)):
            if A[i - 1] < A[i]:
                f[i] += f[i - 1]
            elif A[i - 1] > A[i]:
                g[i] += g[i - 1]

        return max(max(g), max(f))


if __name__ == '__main__':
    c = [5, 4, 2, 1, 3]
    s = Solution()
    r = s.longestIncreasingContinuousSubsequence(c)
    print(r)
