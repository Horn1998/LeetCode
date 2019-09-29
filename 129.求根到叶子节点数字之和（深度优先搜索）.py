#time 97.47 room 5.26

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    count = 0

    def sumNumbers(self, root: TreeNode) -> int:
        if root == None:
            return 0

        def digui(T, num):
            num *= 10
            num += T.val
            if T.left != None:
                digui(T.left, num)
            if T.right != None:
                digui(T.right, num)
            elif T.left == None and T.right == None:
                self.count += num

        digui(root, 0)
        return self.count
