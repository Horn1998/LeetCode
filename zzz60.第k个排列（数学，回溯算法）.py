#效率 18% 空间：5%
class Solustion:
    count = 0
    def getPermutation(self, n,  k):
        target = ""
        for i in range(n):
            target += str(i + 1)
        #判断是否已经找到第k个数字了
        self.judge = 0
        self.n = n
        #记录最终结果
        self.ans, save  = "", ""
        def tacktrace(s, i, k, save):
            #lists求取全排列的数组
            #i+1 个元素进行全排列
            #剪枝
            if self.judge == 1:
                return

            if len(save) == self.n and self.count != k-1:
                self.count += 1
                return
            elif len(save) == self.n and self.count == k - 1:
                self.ans = save
                self.judge = 1
                return
            for t in range(len(s) - 1):
                tacktrace(s[:t] + s[t+1:], i + 1, k, save + s[t])
            if len(s) > 0:
                tacktrace(s[:-1], i + 1, k, save + s[-1])
        tacktrace(target, 0, k, save)
        print(self.ans)
        return self.ans

#正确思路
#递归 回溯 阶乘 数学
def getPermunacation(n, k):
    #记录1-9阶乘的值
    lists = [1]
    def jiecheng(n):
        if n == 1:
            return 1
        return n * jiecheng(n - 1)
    for i in range(1,10):
        lists.append(jiecheng(i))

    print(lists)
    #当前剩余值还差left种
    left = k
    #记录最终结果
    ans = ""
    #当前排列位数不足
    while n > 0:
        count, skip = 0, 0
        for i in range(1,10):
            #如果改数字已经在结果中，则子树中不包含以该树为父节点的子树
            if  str(i) in ans:
                skip += 1
                continue
            #如果当前剩余值小于i*lists[i - 1]个子节点
            elif left <= (i - skip) * lists[n - 1] and str(i) not in ans:
                ans += str(i)
                left = left - (i - skip - 1) * lists[n - 1]
                n = n - 1
                print(ans, left, i, n)
                break

    print(ans)
if __name__ == '__main__':
    s = Solustion()
    s.getPermutation(8,6593)
    getPermunacation(8,6593)


