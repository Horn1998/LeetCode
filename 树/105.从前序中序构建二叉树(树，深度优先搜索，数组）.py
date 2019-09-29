# time:11.75 room:72.84
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    pos = 0

    def buildTree(self, preorder, inorder):
        def digui(child):
            for i in range(len(child)):
                if child[i] == preorder[self.pos]:
                    self.pos += 1
                    T_node = TreeNode(child[i])
                    if i > 0:
                        T_node.left = digui(child[0:i])
                    if i + 1 != len(child):
                        T_node.right = digui(child[i + 1:])
                    return T_node

        t_node = digui(inorder)
        return t_node










