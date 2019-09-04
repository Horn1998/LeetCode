#中等
def groupAnagrams(strs):
    #设定一个中间字符串数组
    temp = []
    #建立一个字典集 键：排序后的字符串，值原始字符串
    dicts = {}
    #遍历字符串数组
    for i in range(len(strs)):
        #对每一个字符串进行排序
        l = list(strs[i])
        l.sort()
        s = "".join(l)
        dicts.setdefault(s,[])
        dicts[s].append(strs[i])
        temp.append(s)
    #对temp进行去重
    temp = list(set(temp))
    #记录最终结果
    ans = []
    #根据键来查找值
    for j in temp:
        ans.append(dicts[j])
    print(ans)

if __name__ == '__main__':
    groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])


