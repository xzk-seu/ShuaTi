class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here
        m = len(A)
        n = len(B)

        f = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                if B[i] == A[j]:
                    f[i + 1][j + 1] = f[i][j] + 1
                else:
                    f[i + 1][j + 1] = max(f[i][j+1], f[i+1][j])
        return f[-1][-1]


if __name__ == '__main__':
    # a = "ABCD"
    # b = "EACB"

    a = "bedaacbade"
    b = "dccaeedbeb"

    """
    "bedaacbade"
    "dccaeedbeb"    
    
    """
    st = Solution()
    r = st.longestCommonSubsequence(a, b)
    print(r)