#room 5 time 90
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    step = 0
    ans = -1 * float('inf')

    def kthSmallest(self, root, k: int) -> int:
        def before_find(root):
            if root == None or self.step == -1:
                return
            before_find(root.left)
            if self.step == -1:
                return
            self.step += 1
            if self.step == k:
                self.ans = root.val
                self.step = -1
                return
            before_find(root.right)

        before_find(root)
        return self.ans

