#时间 42.15 空间 5.24
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    ans =True
    before = -100000000000000
    def isValidBST(self, root: TreeNode) -> bool:
            def valid(root):
                if root == None or self.ans == False:
                    return
                valid(root.left)
                if self.before >= root.val:
                    self.ans = False
                self.before= root.val
                valid(root.right)
            valid(root)
            return self.ans
if __name__ == '__main__':
    s = Solution()
