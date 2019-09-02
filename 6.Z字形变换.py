#字符串运算问题
def convert(s, num):
    ll, ls = [],[]
    count, judge = 0, 0
    #特殊情况，当长度为1时单独讨论
    if num == 1:
        return s

    #将字符串进行分片处理
    while count+num <= len(s):
        if judge == 0:#长分片
            ll.append(s[count:count+num])
            count = count + num
            num = num - 2
            judge = 1
        elif judge == 1:#短分片
            #z字型中间部分倒序排列
            ll.append(("_" + s[count:count+num] + "_")[::-1])
            count = count + num
            num = num + 2
            judge = 0

    #对最后剩余字符串进行单独处理
    add = ""
    if judge == 0:
        ll.append(s[count:])
    elif judge == 1:
        res = ""
        for i in range(num - len(s) + count + 1):#有疑问 没有搞懂
            res += "_"
        ll.append(res + (s[count:])[::-1] + "_")
        num = num + 2
    result = ""

    #重新生成新的字符串
    for step in range(num):
        for item in ll:
            if len(item) > step:
                result += item[step]
    #将字符串中的下划线_去掉
    answer = ""
    for i in result.split("_"):
        answer += i
    return answer



if __name__ == '__main__':
    convert("LEETCODEISHIRING",3)