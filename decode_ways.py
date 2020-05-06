class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """

    def numDecodings(self, s):
        # write your code here
        if len(s) == 0:
            return 0
        f = [0 for _ in range(len(s) + 1)]
        dig = [int(char) for char in s]
        f[0] = 1
        for i in range(1, len(f)):
            if dig[i - 1] > 0:
                f[i] += f[i - 1]
            if i > 1 and 10 <= dig[i - 2] * 10 + dig[i - 1] <= 26:
                f[i] += f[i - 2]
        return f[-1]


if __name__ == '__main__':
    c = "123"
    solution = Solution()
    r = solution.numDecodings(c)
    print(r)
