class Solution:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def maxEnvelopes(self, envelopes):
        # write your code here
        # 按一维排序后，虽然不能保证后面的能装入前面的，但是能保证前面的一定不能装入后面的
        n = len(envelopes)
        envelopes.sort(key=lambda x: [x[0], x[1]])
        f = [1 for _ in envelopes]
        for i in range(1, n):
            e_i = envelopes[i]
            m = 1
            for j in range(i):
                t = f[j] + 1
                e_j = envelopes[j]
                if e_j[0] != e_i[0] and e_j[1] < e_i[1]:
                    m = max(m, t)
                    f[i] = m
        # for i in range(n):
        #     print(envelopes[i], f[i])
        return max(f)


if __name__ == '__main__':
    c = [[15,8],[2,20],[2,14],[4,17],[8,19],[8,9],[5,7],[11,19],[8,11],[13,11],[2,13],[11,19],[8,11],[13,11],[2,13],[11,19],[16,1],[18,13],[14,17],[18,19]]
    s = Solution()
    r = s.maxEnvelopes(c)
    print(r)