#时间98.81
#空间6.44
class Solution:
    def levelOrder(self, root ):
        if root == None:
            return []
        queue ,ans = [], []
        queue.append([root])
        ans.append([root.val])
        while True:
            child = []
            val = []
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
        return ans