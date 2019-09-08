#中等 递归回溯 效率：非常低
import copy
def combinationSum(candidates,target):
    # count表示当前添加的数字在列表中对应的下标
    # left表示当前距离和target还差多少
    candidates.sort()
    count, left = 0, target
    #ans用于记录最终结果
    save, ans = [candidates[0]], []
    if len(candidates) == 1 and candidates[0] == target:
        return [candidates]
    def backtrace(candidates, count, save, left):
        #如果整个列表求和仍然小于target 则直接返回
        if left == 0:
            # #将其加入子列表中
            # save.append(candidates[count])
            #将子列表作为最终结果加入ans中
            save.sort()
            add = copy.deepcopy(save)
            if add  not in ans:
                ans.append(add)
            return
        if count >= len(candidates) or left < 0:
            return
        #当left>0时
        else:
            #当前值不保留继续计算
            for j in range(count + 1, len(candidates)):
                temp = copy.deepcopy(save)
                temp = temp[:-1]
                temp.append(candidates[j])
                print(temp, left, candidates[count], candidates[j], count, j)
                backtrace(candidates, j, temp, left + candidates[count] - candidates[j])

            for j in range(count+1, len(candidates)):
                temp = copy.deepcopy(save)
                temp.append(candidates[j])
                # print(temp,left,candidates[j])
                backtrace(candidates, j, temp, left - candidates[j])
    backtrace(candidates, count, save, left - candidates[count])
    print(ans)
if __name__ == '__main__':
    # combinationSum([14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12],27)

    pass
def next(candidates, target):
    # count表示当前添加的数字在列表中对应的下标
    # left表示当前距离和target还差多少
    candidates.sort()
    count, left = 0, target
    # ans用于记录最终结果
    save, ans = [candidates[0]], []
    if len(candidates) == 1 and candidates[0] == target:
        return [candidates]

    def backtrace(candidates, count, save, left):
        if len(save) == 0 and (candidates[count] == candidates[count - 1]):
            return
        # 如果整个列表求和仍然小于target 则直接返回
        if left == 0:
            # #将其加入子列表中
            # save.append(candidates[count])
            # 将子列表作为最终结果加入ans中
            # save.sort()
            add = copy.deepcopy(save)
            if add not in ans:
                ans.append(add)
            return
        if count >= len(candidates) or left < 0:
            return
        # 当left>0时
        else:
            # 当前值不保留继续计算
            for j in range(count + 1, len(candidates)):
                temp = copy.deepcopy(save)
                temp = temp[:-1]
                temp.append(candidates[j])
                backtrace(candidates, j, temp, left + candidates[count] - candidates[j])

            for j in range(count + 1, len(candidates)):
                temp = copy.deepcopy(save)
                temp.append(candidates[j])
                backtrace(candidates, j, temp, left - candidates[j])

    backtrace(candidates, count, save, left - candidates[count])
    print(ans)
    return ans
next(list(set([14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12])),27)
# list = [14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12]
# list.sort()
# print(set(list))