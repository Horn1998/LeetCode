#time 81 room 5
import copy
class Solution:
    def combinationSum3(self, k, n):
        ans, save = [], []

        def digui(left, step, begin, after, k, save):
            if left < 0 or step > k:
                return
            if left == 0 and k == step:
                ans.append(save)
            for i in range(begin, after + 1):
                if left - i < 0:
                    break
                temp = copy.deepcopy(save)
                temp.append(i)
                digui(left - i, step + 1, i + 1, after, k, temp)

        digui(n, 0, 1, 9, k, [])
        return ans