#参考答案 time 87 room 5.34
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        if root == None:
            return []
        stack, ans = [root, ], []
        while stack != []:
            pre_node = stack.pop()
            ans.append(pre_node.val)
            if pre_node != None:
                if pre_node.right != None:
                    stack.append(pre_node.right)
                if pre_node.left != None:
                    stack.append(pre_node.left)
        return ans
