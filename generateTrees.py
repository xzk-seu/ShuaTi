class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def generateTrees(n: int) -> list:
#     dp = [[[TreeNode(val=i)] if i == j else None for i in range(n + 1)] for j in range(n + 1)]
#     for i in reversed(range(1, n)):
#         for j in range(i + 1, n + 1):
#             dp[i][j] = list()
#             for r in range(i, j+1):
#                 root = TreeNode(val=r)
#                 left = dp[i][r-1] if r > 0 else None
#
#                 root.right = dp[r+1][j] if r < j else None
#     return dp[1][n]


def generateTrees(n: int) -> list:
    if n < 1:
        return []

    def _generate(start: int, end: int) -> list:
        if start > end:
            return [None]
        res = list()
        for r in range(start, end + 1):
            left_list = generate(start, r - 1)
            right_list = generate(r + 1, end)
            for le in left_list:
                for ri in right_list:
                    temp = TreeNode(val=r, left=le, right=ri)
                    res.append(temp)
        return res
    return _generate(1, n)


def generate(start: int, end: int) -> list:
    if start > end:
        return [None]
    res = list()
    for r in range(start, end+1):
        left_list = generate(start, r-1)
        right_list = generate(r+1, end)
        for le in left_list:
            for ri in right_list:
                temp = TreeNode(val=r, left=le, right=ri)
                res.append(temp)
    return res


def print_tree(tree: TreeNode):
    queue = [tree]
    res = [tree.val]
    while len(queue) != 0:
        root = queue.pop(0)
        if not root:
            continue
        queue.append(root.left)
        queue.append(root.right)
        l_val = None if not root.left else root.left.val
        r_val = None if not root.right else root.right.val
        res.append(l_val)
        res.append(r_val)
    print(res)


if __name__ == '__main__':
    tree_list = generateTrees(3)
    for t in tree_list:
        print_tree(t)
