#time 55 room 6.67
class Solution:
    def minSwapsCouples(self, row) -> int:
        def get_partner(pos):
            if pos % 2 == 0:
                return pos + 1
            else:
                return pos - 1

        def get_partner(pos):
            return pos ^ 1

        # 定义待查对象
        ready = []
        # 定义最终结果
        res = 0
        # 已经配对者
        couple = [False for _ in range(len(row))]
        # 开始寻找
        for i in range(len(row) // 2):
            count = 0  # 记录环节点数
            if not couple[2 * i + 1]:  # 落单了，赶紧去找另一半
                waiter = row[2 * i]
                partner, pos = -1, 2 * i + 1
                while partner != waiter:  # 当另一半不是等待者，则另一半对应的同座人继续寻找自己的另一半
                    for j in range(len(row)):
                        if row[j] == get_partner(row[pos]):
                            count += 1
                            pos = get_partner(j)
                            partner = row[j]
                            couple[j] = True
                            couple[pos] = True
                            break
                res += count - 1
        return res

#大神题解
class Solution:
    def minSwapsCouples(self, row) -> int:
        res = 0

        for i in range(0, len(row), 2):
            mate = row[i] ^ 1 #按位异或

            if mate != row[i + 1]:
                j = row[i + 2:].index(mate) + i + 2
                row[i + 1], row[j] = row[j], row[i + 1]
                res += 1
        return res



