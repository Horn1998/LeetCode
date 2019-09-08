#时间 43.73 空间 5.26
def search(nums, target) :
    #时间复杂度 n
    tot0 = 0#记录旋转点
    #特殊情况处理
    if len(nums) == 0:
        return False
    elif len(nums) == 1 and nums[0] == target:
        return True
    elif len(nums) == 1 and nums[0] != target:
        return False
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            tot0 = i + 1
            break
    left, right = 0, len(nums) - 1
    temp =nums[tot0:] + nums[:tot0]
    print(temp)
    while left < right:
        mid = int((left + right) / 2)
        if temp[mid] < target:
            left = mid + 1
        elif temp[mid] > target:
            right = mid - 1
        else:
            left = right = mid
            break
    print(temp[left])
    if temp[left] == target:
        return True
    else:
        return False
if __name__ == '__main__':
    search([2,5,6,0,0,1,2],
5)

