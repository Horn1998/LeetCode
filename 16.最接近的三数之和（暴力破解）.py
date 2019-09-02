#中等 字典操作 效率 低
def threeSumClosest( nums, target) :
    nums.sort()
    dicts = {}
    #构建字典 键：数字 值：数字在字典中的个数
    for i in nums:
        dicts.setdefault(i, 0)
        dicts[i] += 1
    #设置初始误差为0
    error, Continue = 0, True
    while Continue:
        for first in range(len(nums) - 1):
            for second in range(first + 1, len(nums)):
                third = target - nums[first] - nums[second] - error
                #如果要找的第三个数存在字典中，并且在个数为1的情况下不与前两个数相同，在个数为2的情况下，三个数不完全相同
                if third in dicts.keys() and (dicts[third] > 1 or (
                        dicts[third] == 1 and third != nums[first] and third != nums[second])) and not (
                        dicts[third] == 2 and third == nums[first] and third == nums[second]):
                    print(nums[first], nums[second], third)
                    return nums[first] + nums[second] + third
                third = target - nums[first] - nums[second] + error
                if third in dicts.keys() and (dicts[third] > 1 or (
                        dicts[third] == 1 and third != nums[first] and third != nums[second])) and not (
                        dicts[third] == 2 and third == nums[first] and third == nums[second]):
                    print(nums[first], nums[second], third)
                    return nums[first] + nums[second] + third

        error += 1
