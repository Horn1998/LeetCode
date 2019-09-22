#time 99.66  root 5
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        def getChild(start, end):
            childs = []
            if start == end:
                T = TreeNode(start)
                childs.append(T)
                return childs
            for index in range(start, end + 1):
                left_childs, right_childs = [], []
                if index != start:
                    left_childs = getChild(start, index - 1)
                else:
                    left_childs = [None]
                if index != end:
                    right_childs = getChild(index + 1, end)
                else:
                    right_childs = [None]
                for i in left_childs:
                    for j in right_childs:
                        T = TreeNode(index)
                        T.left = i
                        T.right = j
                        childs.append(T)
            return childs

        return getChild(1, n)


