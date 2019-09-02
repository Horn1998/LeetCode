#中等 递归回溯 效率：非常低
import copy
def combinationSum(candidates,target):
    # count表示当前添加的数字在列表中对应的下标
    # left表示当前距离和target还差多少
    count, left = 0, target
    #将候选集进行升序排列
    candidates.sort()
    #ans用于记录最终结果
    save, ans = [], []
    def backtrace(candidates, count, save, left):
        #如果整个列表求和仍然小于target 则直接返回
        if left == 0:
            # #将其加入子列表中
            # save.append(candidates[count])
            #将子列表作为最终结果加入ans中
            ans.append(save)
            return
        if count >= len(candidates):
            return
        #找到最后一个数字

        #表示该子列表永远无法求和构成目标target
        elif left < 0:
            return
        #当left>0时
        else:
            save.append(candidates[count])
            temp = copy.deepcopy(save)
            backtrace(candidates, count, temp, left - candidates[count + 1])
            for j in range(count+1, len(candidates)):
                save = save[:-1]
                save.append(candidates[j])
                temp = copy.deepcopy(save)
                backtrace(candidates, j, temp, left - candidates[j])

    backtrace(candidates, count, save, left)
    print(ans)
if __name__ == '__main__':
    combinationSum([2,3,6,7],7)


#高手题解
def combinationSum(self, candidates, target: int):
    length = len(candidates)
    candidates.sort()
    res = []

    def backtrace(start, tmp_sum, tmp):
        if tmp_sum > target or start == length:
            return
        if tmp_sum == target:
            res.append(tmp)
            return
        for i in range(start, length):
            if tmp_sum + candidates[i] > target:
                break
            backtrace(i, tmp_sum + candidates[i], tmp + [candidates[i]])

    backtrace(0, 0, [])
    return res