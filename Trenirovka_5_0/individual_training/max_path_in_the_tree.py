# На вход дается непустое бинарное дерево.
# Найти максимальную сумму пути в этом дереве.
# "Путь" в бинарном дереве -- последовательность узлов, связанных отношениями родитель--потомок.
# Путь должен содержать как минимум один узел.
# /**
#  * struct TreeNode {
#  *     int val;
#  *     TreeNode *left;
#  *     TreeNode *right;
#  *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
#  * };
#  */
# Пример 1
# Вход:
#        1
#       / \
#      2   3
# Выход: 6
# Пример 2
# Вход:
#    -10
#    / \
#   9  20
#     /  \
#    15   7
# Output: 42
from __future__ import annotations

class TreeNode:
    def __init__(self, val=0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'({self.val}, {self.left}, {self.right})'


def max_path_sum(root: TreeNode | None) -> int:
    ans = float("-inf")

    def traversal(root):
        nonlocal ans
        if not root:
            return 0
        l = traversal(root.left)
        r = traversal(root.right)
        ans = max(ans, r + l + root.val)
        return max(0, l + root.val, r + root.val) # 0 рассматривается из-за того, что могут быть отрицательные суммы в обоих ветвях, и их выкидываем, но вроде ьы он не нужен

    traversal(root)
    return ans


n1 = TreeNode(15)
n2 = TreeNode(7)
n3 = TreeNode(9)
n4 = TreeNode(20, n1, n2)
root = TreeNode(-10, n3, n4)

print(max_path_sum(root))
