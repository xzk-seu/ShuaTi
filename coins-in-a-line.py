class Solution_dp:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        # write your code here
        if n == 0:
            return False
        if n < 3:
            return True
        f = [False for _ in range(n+1)]
        f[1] = True
        f[2] = True
        for i in range(3, n+1):
            f[i] = not (f[i-1] and f[i-2])
        return f[n]


class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        # write your code here
        if n % 3 == 0:
            return False
        return True


if __name__ == '__main__':
    c = int(input())
    st = Solution()
    r = st.firstWillWin(c)
    print(r)
