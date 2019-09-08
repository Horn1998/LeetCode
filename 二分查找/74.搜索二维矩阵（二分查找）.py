#中等 时间：19 空间：5
def searchMatrix(matrix, target):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    len_x = len(matrix)
    len_y = len(matrix[0])
    #利用二叉树进行数字查询
    tot = 0#用于标注当前所在行数
    #当行数没有超过矩阵时
    while len_x > tot:
        #如果target在左子树上
        if target <= matrix[tot][len_y - 1]:
            for i in range(0, len_y):
                #在左子树上查找target
                if target == matrix[tot][i]:
                    print("true")
                    return True
            print("false")
            return False
        else:
            #在左子树上查找
            tot += 1
    print("false")
    return False
if __name__ == '__main__':
    searchMatrix([[]], 13)