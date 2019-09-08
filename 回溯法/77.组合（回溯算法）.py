#时间25.6 空间13.4
import copy
def combine(n, k):
    ans = []
    def traceback(save, num):
        #数组数达到k个 将结果加入结果集
        if len(save) == k:
            ans.append(save)
        #剪枝
        if len(save) > 0 and k - len(save) > n - save[-1]:
            return
        else:
            # 在包含当前num的基础上继续寻找下一个数
            for i in range(num + 1, n + 1):
                temp = copy.deepcopy(save)
                temp.append(i)
                traceback(temp, i)

    traceback([], 0)
    return ans
if __name__ == '__main__':
    combine(1, 1)
