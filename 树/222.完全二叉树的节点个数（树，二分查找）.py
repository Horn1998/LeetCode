#time 80 room 5
class Solution:
    node = 0
    def countNodes(self, root) -> int:
        def digui(root, step):
            if root != None:
                return digui(root.right, step + 1)
            else:
                return step
        def mid_find(root, step, deep):
            if root == None:
                return
            mid_find(root.left, step, deep + 1)
            mid_find(root.right, step, deep + 1)
            if deep == step:
                self.node += 1
        step = digui(root, 0)
        mid_find(root, step, 0)
        self.node += pow(2, step) - 1
        return self.node