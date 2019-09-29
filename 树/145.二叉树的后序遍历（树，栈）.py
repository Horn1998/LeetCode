#困难 time 71.75 room  5.37
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        if root == None:
            return []
        roots, ans = [root, ], []
        root.val == -1.1
        while not (roots == [] and (root.left == None or root.left.val == -1.1) and (
                root.right == None or root.right.val == -1.1)):
            if root.left != None and root.left.val != -1.1:
                roots.append(root)
                root = root.left
            elif root.right != None and root.right.val != -1.1:
                roots.append(root)
                root = root.right
            else:
                ans.append(root.val)
                root.val = -1.1
                root = roots.pop()

        return ans