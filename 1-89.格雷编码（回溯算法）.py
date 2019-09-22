#时间 25.08 空间5.17
def grayCode(n):
    #记录每一个子值
    lists = [0,1]   
    ans = []
    #共进行n-1轮操作
    for i in range(1, n):
        #记录上一轮得到结果的长度
        len_before = len(lists)
        temp = list(reversed(lists))
        lists = lists + temp
        print(lists)
        # for j in range(len_before):
        #     lists[j] = lists[j]
        for j in range(len_before, 2*len_before):
            lists[j] = pow(2, i)+ lists[j]
    # for i in range(len(lists)):
    #     count = 0#用来获取实际值
    #     for j in range(len(lists[i])):
    #         count += int(lists[i][j]) * pow(2,len(lists[i]) - j - 1)
    #     ans.append(count)
    print(lists)
    return ans
if __name__ == '__main__':
    grayCode(3)