class Solution:
    """
    @param nums: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    """

    def houseRobber2(self, nums):
        # write your code here
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        f = [0 for _ in range(len(nums))]
        f[1] = nums[0]
        # 0 -> n-2, 不偷n-1
        for i in range(2, len(nums)):
            f[i] = max(f[i - 1], f[i - 2] + nums[i - 1])
        temp = f[-1]

        # 1 -> n-1, 不偷0
        f = [0 for _ in range(len(nums))]
        f[1] = nums[1]
        for i in range(2, len(nums)):
            f[i] = max(f[i - 1], f[i - 2] + nums[i])

        return max(f[-1], temp)


if __name__ == '__main__':
    c = [2, 3, 2, 3]
    c = [2]
    s = Solution()
    r = s.houseRobber2(c)
    print(r)
