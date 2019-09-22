#time 5.03 room 74.17
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    pos = 0

    def buildTree(self, inorder, postorder):
        self.pos = len(postorder) - 1

        def digui(nums):
            for i in range(len(nums)):
                if nums[i] == postorder[self.pos]:
                    self.pos -= 1
                    T = TreeNode(nums[i])
                    if i != len(nums) - 1:
                        T.right = digui(nums[i + 1:])
                    if i != 0:
                        T.left = digui(nums[0:i])
                    return T

        return digui(inorder)

