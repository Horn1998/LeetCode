#单调栈问题 time 90 room 8
#解题思路
'''
定义单调栈，对于每个元素，先通过单调栈求出左侧大于等于该元素的元素个数left，再通过循环求出右侧大于该元素的元素个数right,以该元素为最小值的所有子序列
            求和为 min * (left + 1) * (right + 1)
'''
class Solution:
    def sumSubarrayMins(self, A) -> int:
        #定义单调栈
        st = []
        A.append(0)
        length = len(A)
        #定义左侧数组
        left = [1 for _ in range(length)]
        #定义结果
        res = 0
        #开始计算
        for i in range(length):
            #单调递增栈
            if st and A[i] < A[st[-1]]:
                while st and A[i] < A[st[-1]]:
                    top = st.pop()
                    res += A[top] * (i - top) * left[top]
                st.append(i)
                left[i] = i - top + left[top]
            else:
                st.append(i)
        return res % (10 **9 + 7)