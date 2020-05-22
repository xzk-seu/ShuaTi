class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        n = len(nums)
        if n == 0:
            return 0
        f = [1 for _ in nums]

        res = 0
        for i in range(1, n):
            m = 1
            for j in range(i):
                t = f[j] + 1
                if nums[i] > nums[j] and t > m:
                    m = t
                    f[i] = m
            res = max(res, m)
        return res


        # for n, i in enumerate(nums[1:]):
        #     m = 0
        #     for j in range(n+1):
        #         t = f[j] + 1
        #         if i > nums[j] and t > m:
        #             m = t
        #             f[i] = m
        # print(f)
        # return max(f)


if __name__ == '__main__':
    c = [5,4,1,2,3]
    s = Solution()
    r = s.longestIncreasingSubsequence(c)
    print(r)
