#时间 19.79 空间 5
def removeDuplicates(nums):
    tot1 = 0 #用于作为nums中的每一个新元素的计数标志
    count = len(nums) #用于记录去重后数组的长度
    #长度为0需要单独处理
    if len(nums) <= 1:
        return 1
    #当nums长度大于1时
    i = 1
    while i>=1 and i < count:
        if nums[i - 1] == nums[i]:
            tot1 += 1
            if tot1 > 2:
                count -= 1
                for k in range(i, count):
                    nums[k], nums[k+1] = nums[k+1],nums[k]
                i -= 1
            i += 1
        else:
            tot1 = 1#记录当前重复数字个数
            i += 1
    print(nums)
    print(count)
if __name__ == '__main__':
    removeDuplicates([0,0,1,1,1,1,2,3,3])

