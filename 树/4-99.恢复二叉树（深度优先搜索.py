#time 55 room 6  hard
'''
解题思路
本题利用搜索二叉树中序遍历单调递增特点
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 本题利用二叉搜索树中序遍历数值单调递增特点
        node = [None, None]
        ans = []

        def mid_find(root):
            if root == None:
                return
            mid_find(root.left)
            if ans and ans[-1].val > root.val and not node[0]:
                node[1] = root #邻近两点位置互换
                node[0] = ans[-1]
                ans.append(root)
            elif ans and ans[-1].val > root.val:
                node[1] = root #非邻近两点位置互换
            else:
                ans.append(root)

            mid_find(root.right)
        mid_find(root)
        node[0].val, node[1].val = node[1].val, node[0].val