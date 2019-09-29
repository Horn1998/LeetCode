#时间：72.36 空间8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        if root == None:
            return []
        queue ,ans = [], []
        left = False
        queue.append([root])
        ans.append([root.val])
        while True:
            child = []
            val = []
            if left:
                left = False
                for i in range(len(queue[-1])):
                    node = queue[-1][i]
                    if node.left != None :
                        child.append(node.left)
                        val.append(node.left.val)
                    if node.right != None:
                        child.append(node.right)
                        val.append(node.right.val)
                if len(child)!=0:
                    queue.append(child)
                    ans.append(val)
                else:
                    break
            else:
                left = True
                for i in range(len(queue[-1])-1, -1, -1):
                    node = queue[-1][i]
                    if node.right != None:
                        child = [node.right] + child
                        val.append(node.right.val)
                    if node.left != None :
                        child = [node.left] + child
                        val.append(node.left.val)
                if len(child)!=0:
                    queue.append(child)
                    ans.append(val)
                else:
                    break
        return ans