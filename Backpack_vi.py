class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPackVI(self, nums, target):
        # write your code here
        f = [0 for _ in range(target + 1)]
        f[0] = 1

        for i in range(1, target + 1):
            for n in nums:
                if n <= i:
                    f[i] += f[i-n]

        return f[target]


class Solution_way:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPackVI(self, nums, target):
        # write your code here
        f = [0 for _ in range(target + 1)]
        pai = [0 for _ in range(target + 1)]
        f[0] = 1

        for i in range(1, target + 1):
            for n in nums:
                if n <= i:
                    f[i] += f[i-n]
                    pai[i] = n

        t = target
        temp_list = list()
        while t > 0:
            temp_list.append(pai[t])
            t -= pai[t]
        print(temp_list)

        return f[target]


if __name__ == '__main__':
    p1 = [1, 2]
    p2 = 4
    st = Solution()
    r = st.backPackVI(p1, p2)
    print(r)

    st = Solution_way()
    r = st.backPackVI(p1, p2)
    print(r)
