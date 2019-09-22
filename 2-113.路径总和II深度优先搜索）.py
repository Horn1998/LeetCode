import copy
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum)  :
        results = []

        def dp(t_node, child, sums):
            if t_node == None:
                return
            elif t_node.val + sums == sum and t_node.left == None and t_node.right == None:
                copy_child = copy.deepcopy(child)
                copy_child.append(t_node.val)
                results.append(copy_child)
                return
            else:
                copy_child = copy.deepcopy(child)
                copy_child.append(t_node.val)
                sums += t_node.val
                dp(t_node.left, copy_child, sums)
                dp(t_node.right, copy_child, sums)

        dp(root, [], 0)
        return results