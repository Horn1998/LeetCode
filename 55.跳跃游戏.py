#内存消耗过大
def canJump(nums):
    #游标
    tot = -1
    #判断是否查找下一个0的位置
    judge = 1
    for i in range(len(nums) - 1, -1 , -1):
        if nums[i] == 0 and judge != 0:
            judge = 0
            tot = i
        elif judge == 0:
            if tot - i < nums[i]:
                judge = 1
                print(nums[i])
        elif nums[i] != 0 and judge == 1:
            continue
    if judge == 0:
        print('false')
        return False
    else:
        print('true')
        return True
if __name__ == '__main__':
    canJump( [2,0,1,0,1])


#二刷 效率没有之前的高，但是代码量要少-
def canJump(nums):
    start, end = 0, 0
    n = len(nums)
    while start <= end and end < len(nums - 1):
        end = max(end, nums[start] + start)
        start += 1
    return  end >= n - 1


canJump([3,2,1,0,4])