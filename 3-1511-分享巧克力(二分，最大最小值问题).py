#题解 time 30
'''
1231. 分享巧克力  显示英文描述

你有一大块巧克力，它由一些甜度不完全相同的小块组成。我们用数组 sweetness 来表示每一小块的甜度。

你打算和 K 名朋友一起分享这块巧克力，所以你需要将切割 K 次才能得到 K+1 块，每一块都由一些 连续 的小块组成。

为了表现出你的慷慨，你将会吃掉 总甜度最小 的一块，并将其余几块分给你的朋友们。

请找出一个最佳的切割策略，使得你所分得的巧克力 总甜度最大，并返回这个 最大总甜度。


'''
class Solution:
    def maximizeSweetness(self, sweetness, K: int) -> int:
        if not K: return sum(sweetness)
        Max_sweet = sum(sweetness)
        Min_sweet = min(sweetness)
        Max_eat = int(sum(sweetness) / K) + 1

        def judge(sweet_scale):
            now, k = 0, 0
            for i in sweetness:
                now += i
                if now >= sweet_scale:
                    now, k = 0, k + 1
            return k

        left, right = Min_sweet, Max_eat
        while left < right:
            mid = left + (right - left + 1) // 2
            if judge(mid) >= K + 1:
                left = mid
            else:
                right = mid - 1

        return left
