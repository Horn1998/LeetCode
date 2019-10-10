#time 99 room 5
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#设置三个bool值 left:左子树是否有目标值， right:右孩子是否有目标值 mid:自身是否有目标值
#当三个布尔值中有两个为true时，该节点便是我们要找的最先父节点
#本题尝试用广度优先遍历与二叉树性质进行计算，但是由于节点在二叉树中位置对应数字超出float的处理范围，故舍弃
class Solution:
    ans = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def digui(root, left, right):
            if root == None or self.ans:
                return False
            left = digui(root.left, False, False)
            right = digui(root.right, False, False)
            judge = 0
            if left == True:
                judge += 1
            if right == True:
                judge += 1
            if root == p or root == q:
                judge += 1
            if judge >= 2:
                self.ans = root
            if root == p or root == q or left == True or right == True:
                return True

        digui(root, False, False)
        return self.ans
