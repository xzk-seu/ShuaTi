class Solution:
    """
    @param num: a non negative integer number
    @return: an array represent the number of 1's in their binary
    """
    def countBits(self, num):
        # write your code here
        f = [0 for _ in range(num+1)]
        for i in range(1, num+1):
            p = i >> 1
            f[i] = f[p] + (i % 2)
        return f


if __name__ == '__main__':
    c = 5
    s = Solution()
    r = s.countBits(c)
    print(r)
