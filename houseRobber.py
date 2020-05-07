class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        # write your code here
        f = [0 for _ in range(len(A) + 1)]

        for i in range(1, len(A) + 1):
            f[i] = max(f[i - 1], f[i - 2] + A[i - 1])

        return f[-1]


if __name__ == '__main__':
    c = [5, 2, 1, 3]
    s = Solution()
    r = s.houseRobber(c)
    print(r)
