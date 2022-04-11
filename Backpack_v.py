class Solution_not_opt:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPackV(self, nums, target):
        # write your code here
        # f[i][w]表示到前i个物品，拼出w的次数
        n = len(nums)
        f = [[0 for _ in range(target+1)] for _ in range(n+1)]
        for t in f:
            t[0] = 1
        for i, a in enumerate(nums):
            for j in range(target+1):
                f[i+1][j] = f[i][j] + (f[i][j - a] if a <= j else 0)

        # for i, j in enumerate(reversed(f[-1])):
        #     if j:
        #         return m-i
        return f[-1][-1]


class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPackV(self, nums, target):
        # write your code here
        # f[i][w]表示到前i个物品，拼出w的次数
        n = len(nums)
        f = [0 for _ in range(target + 1)]
        f[0] = 1

        for i in range(n-1):
            for j in reversed(range(1, target + 1)):
                temp = j - nums[i]
                if temp >= 0:
                    f[j] += f[temp]
        temp = target - nums[-1]
        res = f[-1]
        if temp >= 0:
            res += f[temp]
        return res


if __name__ == '__main__':
    p1 = [1,2,3,3,7]
    p2 = 7
    st = Solution()
    r = st.backPackV(p1, p2)
    print(r)
