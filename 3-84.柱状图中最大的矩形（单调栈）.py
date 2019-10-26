#time 92 room 27
'''
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
'''
class Solution:
    def largestRectangleArea(self, heights) -> int:
        # 单调栈
        #简化计算
        heights += [0]
        st = [-1]
        # 最终结果
        res = 0
        for i in range(len(heights)):
            # 单调递增栈,入栈
            if st and heights[st[-1]] <= heights[i]:
                st.append(i)
            # 出栈
            elif st and heights[st[-1]] > heights[i]:
                top = st[-1]
                while heights[st[-1]] > heights[i]:
                    top = st.pop()
                    # 计算宽度
                    width = i - top
                    res = max(width * heights[top], res)
                st.append(top)
                heights[top] = heights[i]
        return res
