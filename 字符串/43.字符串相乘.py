def multiply(num1, num2):
    #记录两个字符串的长度
    l1 = len(num1)
    l2 = len(num2)
    #num1 为第一个乘数， num2为第二个乘数
    #设置arr为记录结果的数组
    arr = [[0 for col in range(len(num2) + len(num1))] for row in range(len(num2))]
    left = 0
    #开始计算
    for i in range(len(num2)-1, -1, -1):
        for j in range(len(num1) - 1, -1, -1):
            res = int(num2[i]) * int(num1[j])
            arr[len(num2) - i - 1][len(num1) - j - 1 + len(num2) - i - 1] = res

    print(arr)
    #记录结果
    ans = ""
    count = 0
    for j in range(len(num1) + len(num2)):
        for k in range(len(num2)):
            count += arr[k][j]
        print(k, j, count)
        count = count + left
        ans = str(int(count%10)) + ans
        left = int (count / 10)
        count = 0
    if left != 0:
        ans = str(left) + ans
    for i in range(len(ans)):
        if ans[i] == '0' and len(ans)!= 1:
            ans = ans[1:]
        else:
            break
    print(ans)
    return ans
if __name__ == '__main__':
    multiply("123","456")
