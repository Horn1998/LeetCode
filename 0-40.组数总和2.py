#time 7.65 room 5.4
import copy
class Solution:
    def combinationSum2(self, candidates, target: int):
        candidates.sort()

        def backtrack(target, start, c_arr):
            if sum(c_arr) == target:
                temp = copy.deepcopy(c_arr)
                if temp not in ans:
                    ans.append(temp)
            elif sum(c_arr) > target:
                return

            for index in range(start, len(candidates)):
                c_arr.append(candidates[index])
                backtrack(target, index + 1, c_arr)
                c_arr.pop()

        ans = []
        backtrack(target, 0, [])
        return ans
