#time 92.99 room 6.10
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    deep = 0

    def rightSideView(self, root):
        if root == None:
            return []
        ans = []

        def see_tr(root):
            ans.append(root.val)
            if root.right != None:
                self.deep += 1
                see_tr(root.right)
            elif root.left != None:
                self.deep += 1
                see_tr(root.left)

        def see_tl(root, depth):
            if self.deep < depth:
                ans.append(root.val)
                self.deep = depth
            if root.right != None:
                see_tl(root.right, depth + 1)
            if root.left != None:
                see_tl(root.left, depth + 1)

        see_tr(root)
        see_tl(root, 0)
        return ans
