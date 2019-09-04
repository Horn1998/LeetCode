#中等
def fourSum(nums, target):
    tot1 = 0 #记录起始位置
    tot3 = len(nums) - 1#记录最终位置
    tot2 = tot1 + 1#中间移动指针
    nums.sort()#将数组按照升序排列
    dicts = {} #记录数组中值的位置
    ans = [] #记录最终结果

    #对nums中存在的值生成字典
    for i in range(len(nums)):
        dicts.setdefault(nums[i],[])
        dicts[nums[i]].append(i)

    def judge(list, j, tot):
        for k in list:
            if k > j and k <= tot:
                return True#表示存在第四个数
        return False

    temp = target
    while tot1 <= len(nums) - 4:
        while tot1 <= tot3 - 3:#从外向内查找组合
            target = temp
            target -= nums[tot1] + nums[tot3]
            j = tot2
            while j < tot3:
                # print(target-nums[j], j, tot3 -1, dicts[target - nums[j]])
                if target - nums[j] in dicts.keys() and judge(dicts[target-nums[j]], j,  tot3-1):
                    ans.append([nums[tot1], nums[j],target - nums[j], nums[tot3]])
                while nums[j] == nums[j+1] and j < tot3 - 1:
                    j = j + 1
                j += 1

            while nums[tot3] == nums[tot3 - 1] and tot3 > 3:
                tot3 -= 1
            tot3 -= 1

        #tot1右移
        while nums[tot1] == nums[tot1 + 1] and tot1 <= len(nums) - 4:
            tot1 += 1
        tot1 += 1
        tot2 = tot1 + 1
        tot3 = len(nums) - 1
    print(ans)
if __name__ == '__main__':
    fourSum([-3,-2,-1,0,0,1,2,3], 0)

